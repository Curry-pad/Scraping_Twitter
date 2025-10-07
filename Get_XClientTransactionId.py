#https://pypi.org/project/xclienttransaction/
#できたぞ！！！XCTIの生成もできてる！！！
def Get_XClientTransactionId(
  url,method
):

  #まずはTwitterの入り口部分にアクセスして、XCTIの取得に必要な情報（ondemand_file_response）を取得する
  import bs4
  import requests
  from x_client_transaction.utils import generate_headers, handle_x_migration, get_ondemand_file_url
  
  # INITIALIZE SESSION
  session = requests.Session()
  session.headers = generate_headers()
  
  
  # GET HOME PAGE RESPONSE
  # required only when hitting twitter.com but not x.com
  # returns bs4.BeautifulSoup object
  home_page_response = handle_x_migration(session=session)
  
  # for x.com no migration is required, just simply do
  home_page = session.get(url="https://x.com")
  home_page_response = bs4.BeautifulSoup(home_page.content, 'html.parser')
  
  
  # GET ondemand.s FILE RESPONSE
  ondemand_file_url = get_ondemand_file_url(response=home_page_response)
  ondemand_file = session.get(url=ondemand_file_url)
  ondemand_file_response = bs4.BeautifulSoup(ondemand_file.content, 'html.parser')

  #とりあえずここまで、特にエラーにはならない。
  print("オンデマンドファイルURL：",ondemand_file_url)
  print("オンデマンドファイル：",ondemand_file)
  #↓これを印字しようとすると、長くて真っ赤なログが出る。エラーになっているわけではなさそうだけど…。
  #print("オンデマンドファイルレスポンス：",ondemand_file_response)
  
  from urllib.parse import urlparse
  from x_client_transaction import ClientTransaction
  
  # replace the url and http method as per your use case
  path = urlparse(url=url).path
  print("path:",path)
  # path will be /i/api/1.1/jot/client_event.json in this case

  #x-client-transaction-idを生成する！！
  ct = ClientTransaction(home_page_response=home_page_response, ondemand_file_response=ondemand_file_response)
  transaction_id = ct.generate_transaction_id(method=method, path=path)
  
  print("生成されたx-client-transaction-id：",transaction_id)

  #XCTIをレスポンスとして返却
  return {
    "url" : url
    "method" : method
    "created_XCTI" : transaction_id
  }
  

