#https://qiita.com/jasoncitronx/items/74b4ebcb20814729dbd0
def Twikit_Login(
  user_name,password
):
  
  # with文で書き込む方法もあるが、今回は省略
  from twikit import Client

  # Initialize client
  client = Client('ja-JP')
  
  async def main():
      await client.login(
          auth_info_1=user_name,
          #auth_info_2=EMAIL,
          password=password,
          #cookies_file='cookies.json'
      )
  
  asyncio.run(main())
  
  # ログイン情報を cookies.json に保存する
  client.save_cookies("cookies.json")
  
