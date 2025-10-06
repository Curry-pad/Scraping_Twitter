
def Get_XClientTransactionId(
  endPointURL
):

  #まずはTwitterの入り口部分にアクセスして、XCTIの取得に必要な情報（ondemand_file_response）を取得する
  
  import bs4
  import requests
  from x_client_transaction.utils import generate_headers, handle_x_migration, get_ondemand_file_url
  
  # INITIALIZE SESSION
  session = requests.Session()
  session.headers = generate_headers()

  print('ヘッダー：',session.headers)
  
  # GET HOME PAGE RESPONSE
  # required only when hitting twitter.com but not x.com
  # returns bs4.BeautifulSoup object
  home_page_response = handle_x_migration(session=session)

  print('ホームページレスポンス①',home_page_response)
  
  # for x.com no migration is required, just simply do
  home_page = session.get(url="https://x.com")
  home_page_response = bs4.BeautifulSoup(home_page.content, 'html.parser')

  print('ホームページレスポンス②',home_page_response)

  return home_page_response
  
  # GET ondemand.s FILE RESPONSE
  ondemand_file_url = get_ondemand_file_url(response=home_page_response)
  ondemand_file = session.get(url=ondemand_file_url)
  ondemand_file_response = bs4.BeautifulSoup(ondemand_file.content, 'html.parser')

  print(ondemand_file_response)

