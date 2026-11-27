import base64
import math
import re
#requests追加
import requests
from typing import Union

import bs4

#新形式のファイルを見つけるための正規表現
JS_FILE_REGEX = re.compile(
    r"https://abs.twimg.com/x-web/x-web/assets/[^\"']+.js"
)

from .constants import MIGRATION_REDIRECTION_REGEX, ON_DEMAND_FILE_REGEX, ON_DEMAND_FILE_URL, ON_DEMAND_HASH_PATTERN


class Math:

    @staticmethod
    def round(num: Union[float, int]):
        # using javascript...? just use the native Math.round(num)
        x = math.floor(num)
        if (num - x) >= 0.5:
            x = math.ceil(num)
        return math.copysign(x, num)


def generate_headers():
    headers = {"Authority": "x.com",
               "Accept-Language": "en-US,en;q=0.9",
               "Cache-Control": "no-cache",
               "Referer": "https://x.com",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
               "X-Twitter-Active-User": "yes",
               "X-Twitter-Client-Language": "en"}
    return headers


def validate_response(response: bs4.BeautifulSoup):
    if not isinstance(response, bs4.BeautifulSoup):
        raise TypeError(
            f"the response object must be bs4.BeautifulSoup, not {type(response).__name__}")


def get_migration_url(response: bs4.BeautifulSoup):
    migration_url = response.select_one("meta[http-equiv='refresh']")
    migration_redirection_url = re.search(MIGRATION_REDIRECTION_REGEX, str(
        migration_url)) or re.search(MIGRATION_REDIRECTION_REGEX, str(response.content))
    return migration_redirection_url


def get_migration_form(response: bs4.BeautifulSoup):
    migration_form = response.select_one("form[name='f']") or response.select_one(
        f"form[action='https://x.com/x/migrate']")
    if not migration_form:
        return
    url = migration_form.attrs.get("action", "https://x.com/x/migrate")
    method = migration_form.attrs.get("method", "POST")
    request_payload = {input_field.get("name"): input_field.get(
        "value") for input_field in migration_form.select("input")}
    return {"method": method, "url": url, "data": request_payload}


def get_ondemand_file_url(response: bs4.BeautifulSoup):
    
    print(
        "これは自前の関数「get_ondemand_file_url」です。自由に改造することができます。"
    )

    html = str(response)

    #
    # 旧形式
    #
    match = ON_DEMAND_FILE_REGEX.search(html)

    if match:

        on_demand_file_index = match.group(1)

        regex = re.compile(
            ON_DEMAND_HASH_PATTERN.format(on_demand_file_index)
        )

        filename = regex.search(html).group(1)

        return ON_DEMAND_FILE_URL.format(
            filename=filename
        )

    #
    # 新形式
    #
    print("ondemand.s が見つからないため、新形式探索を開始します")

    new_style_url = find_new_style_js(html)

    if new_style_url:
        return new_style_url

    raise Exception("ondemand file not found")



def find_new_style_js(html):

    print("========== HTML調査 ==========")
    print("abs.twimg.com" in html)
    print("x-web" in html)
    print(".js" in html)
    print(html[html.find("https://abs.twimg.com/x-web/x-web/assets/")-100 :
        html.find("https://abs.twimg.com/x-web/x-web/assets/")+300])

    print("========== JS探索 ==========")
    js_urls = JS_FILE_REGEX.findall(html)
    print(f"件数:{len(js_urls)}")
    
    for js_url in js_urls:

        try:
            print(f"チェック中:{js_url}")
            
            js_text = requests.get(
                js_url,
                timeout=10
            ).text

            if INDICES_REGEX.search(js_text):
                print(f"発見:{js_url}")
                print(matches[:10])
                return js_url
            
        except Exception as ex:
            print(ex)
            continue

    return None

def handle_x_migration(session):
    # for python requests -> session = requests.Session()
    # session.headers = generate_headers()
    response = session.request(method="GET", url="https://x.com/home")
    home_page = bs4.BeautifulSoup(response.content, 'html.parser')
    migration_redirection_url = get_migration_url(response=home_page)
    if migration_redirection_url:
        response = session.request(
            method="GET", url=migration_redirection_url.group(0))
        home_page = bs4.BeautifulSoup(response.content, 'html.parser')
    migration_form = get_migration_form(response=home_page)
    if migration_form:
        response = session.request(**migration_form)
        home_page = bs4.BeautifulSoup(response.content, 'html.parser')
    return home_page


async def handle_x_migration_async(session):
    # for httpx -> session = httpx.AsyncClient(headers=generate_headers())
    response = await session.request(method="GET", url="https://x.com/home")
    home_page = bs4.BeautifulSoup(response.content, 'html.parser')
    migration_redirection_url = get_migration_url(response=home_page)
    if migration_redirection_url:
        response = await session.request(method="GET", url=migration_redirection_url.group(0))
        home_page = bs4.BeautifulSoup(response.content, 'html.parser')
    migration_form = get_migration_form(response=home_page)
    if migration_form:
        response = await session.request(**migration_form)
        home_page = bs4.BeautifulSoup(response.content, 'html.parser')
    return home_page


def float_to_hex(x):
    result = []
    quotient = int(x)
    fraction = x - quotient

    while quotient > 0:
        quotient = int(x / 16)
        remainder = int(x - (float(quotient) * 16))

        if remainder > 9:
            result.insert(0, chr(remainder + 55))
        else:
            result.insert(0, str(remainder))

        x = float(quotient)

    if fraction == 0:
        return ''.join(result)

    result.append('.')

    while fraction > 0:
        fraction *= 16
        integer = int(fraction)
        fraction -= float(integer)

        if integer > 9:
            result.append(chr(integer + 55))
        else:
            result.append(str(integer))

    return ''.join(result)


def is_odd(num: Union[int, float]):
    if num % 2:
        return -1.0
    return 0.0


def base64_encode(string: str):
    string = string.encode() if isinstance(string, str) else string
    return base64.b64encode(string).decode()


def base64_decode(input):
    try:
        data = base64.b64decode(input)
        return data.decode()
    except Exception:
        # return bytes(input, "utf-8")
        return list(bytes(input, "utf-8"))


if __name__ == "__main__":
    pass
