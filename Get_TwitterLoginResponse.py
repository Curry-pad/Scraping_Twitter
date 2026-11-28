import re
from pathlib import Path
# ["可変部分"].forEach(function(name){var href="https://abs.twimg.com/x-web/x-web/assets/"+name+".js"
PATTERN = re.compile(
    r'\["([^"]+)"\]\.forEach\(function\(name\)\{var href="https://abs\.twimg\.com/x-web/x-web/assets/"\+name\+"\.js"'
)

def Get_TwitterLoginResponse(
  ct0,auth_token
):
  
  import bs4
  import requests
  import datetime
  from fastapi import HTTPException
  
  #from x_client_transaction.utils import generate_headers, handle_x_migration, get_ondemand_file_url
  from x_client_transaction.utils import generate_headers, handle_x_migration

  #2026/11/25　get_ondemand_file_url関数に欠陥あり、この関数だけ自前にしてみる
  from XClientTransaction.utils import get_ondemand_file_url

  try:
    
    #Twitterの入り口部分にアクセスして、XCTIの取得に必要な情報（ondemand_file_response）を取得する
    # INITIALIZE SESSION
    session = requests.Session()
    session.headers = generate_headers()
    
    # 2026/09/26　ct0とauth_token（=ユーザの認証情報）が必須になったようなので追加
    session.cookies.set("auth_token",auth_token)
    session.cookies.set("ct0",ct0)
      
    # GET HOME PAGE RESPONSE
    # required only when hitting twitter.com but not x.com
    # returns bs4.BeautifulSoup object
    home_page_response = handle_x_migration(session=session)
  
    print(type(home_page_response))
    #print(str(home_page_response)[:1000])
      
    html = str(home_page_response)

    ondemand_urls = extract_js_urls(html)

  except Exception as e:
    raise HTTPException(
      status_code=500,
      detail=str(e)
    )
  
  #htmlをレスポンスとして返却
  return {
    "ondemand_urls" : ondemand_urls
  }

def extract_js_urls(html: str) -> list[str]:
    urls = []
    # 1. 全体の文字列をセミコロンで区切る
    for chunk in html.split(";"):
        # 2. 正規表現で探して可変部分を取得
        match = PATTERN.search(chunk)
        if match:
            module_id = match.group(1)
            # 3. 合体させて完成
            url = f"{BASE_URL}{module_id}.js"
            if url not in urls:
                urls.append(url)
    return urls



