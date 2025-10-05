#https://qiita.com/jasoncitronx/items/74b4ebcb20814729dbd0
def Twikit_Login(
  user_name,password
):
  
  # with文で書き込む方法もあるが、今回は省略
  from twikit import Client
  
  client = Client("ja-JP")
  
  client.login(
    auth_info_1=user_name,
    password=password
  )
  
  # ログイン情報を cookies.json に保存する
  client.save_cookies("cookies.json")
  
