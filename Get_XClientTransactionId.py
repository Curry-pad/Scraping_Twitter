import bs4
from x_client_transaction import ClientTransaction

#https://pypi.org/project/xclienttransaction/
#できたぞ！！！XCTIの生成もできてる！！！
def Get_XClientTransactionId(
  ct0,auth_token,url,method
):
  
  import requests
  import datetime
  import traceback
  
  from fastapi import HTTPException
  
  #from x_client_transaction.utils import generate_headers, handle_x_migration, get_ondemand_file_url
  from x_client_transaction.utils import generate_headers, handle_x_migration

  #2026/11/25　get_ondemand_file_url関数に欠陥あり、この関数だけ自前にしてみる
  from XClientTransaction.utils import get_ondemand_file_url

  try:
    
    #まずはTwitterの入り口部分にアクセスして、XCTIの取得に必要な情報（ondemand_file_response）を取得する
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

    #output_FileName = datetime.datetime.now().strftime(
    #  "XCTI_html_%Y%m%d_%H%M%S.html"
    #)
    #with open(output_FileName, "w", encoding="utf-8") as f:
    #  f.write(html)
    #print("htmlファイル名☟")
    #print(output_FileName)

    #html全部出していいっすか！？→でかすぎて見づらい…
    #print(html)

    #print("「home_page_response」の最後の3000行☟")
    #print(html[-3000:])
    print("HTML length:", len(html))
    print("ondemand.s:", "ondemand.s" in html)
    print("ondemand:", "ondemand" in html)
      
    for keyword in ["ondemand.s", "ondemand", "webpack", "main.js"]:
      print(keyword, html.find(keyword))
      
    # for x.com no migration is required, just simply do
    # home_page = session.get(url="https://x.com/home")
    # home_page_response = bs4.BeautifulSoup(home_page.content, 'html.parser')
      
      
    # GET ondemand.s FILE RESPONSE
    ondemand_file_url = get_ondemand_file_url(response=home_page_response)
    ondemand_file = session.get(url=ondemand_file_url)
      
    #ondemand_file_response = bs4.BeautifulSoup(ondemand_file.content, 'html.parser')
    ondemand_file_response = ondemand_file.text
    
    #とりあえずここまで、特にエラーにはならない。
    print("オンデマンドファイルURL：",ondemand_file_url)
    print("オンデマンドファイル：",ondemand_file)
    #↓これを印字しようとすると、長くて真っ赤なログが出る。エラーになっているわけではなさそうだけど…。
    #print("オンデマンドファイルレスポンス：",ondemand_file_response)
      
    from urllib.parse import urlparse
      
    # replace the url and http method as per your use case
    path = urlparse(url=url).path
    print("path:",path)
    # path will be /i/api/1.1/jot/client_event.json in this case
    
    #x-client-transaction-idを生成する！！
    #ct = ClientTransaction(home_page_response=home_page_response, ondemand_file_response=ondemand_file_response)

    ct = CustomClientTransaction(
      home_page_response=home_page_response,
      ondemand_file_response=ondemand_file_response,
    )
    
    transaction_id = ct.generate_transaction_id(method=method, path=path)
      
    print("生成されたx-client-transaction-id：",transaction_id)

  except Exception as e:
    print("=== エラー詳細 ===")
    traceback.print_exc()
    raise HTTPException(
        status_code=500,
        detail=f"{type(e).__name__}: {e}",
    )
  
  #XCTIをレスポンスとして返却
  return {
    "url" : url,
    "method" : method,
    "created_XCTI" : transaction_id
  }

#サブクラス
class CustomClientTransaction(ClientTransaction):
    def get_frames(self, home_page_response: bs4.BeautifulSoup) -> bs4.ResultSet:
        # loading-x-anim-0 ... loading-x-anim-3 の <svg> だけを取得する
        return home_page_response.select("svg[id^='loading-x-anim']")

