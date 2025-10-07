#https://qiita.com/jasoncitronx/items/74b4ebcb20814729dbd0
def Twikit_Login(
  user_name,EMAIL,pass_word
):

  from twikit import Client
  import asyncio

  # Initialize client
  client = Client('ja')

  print("ユーザ名：",user_name)
  print("パスワード：",pass_word)
  
  async def main():
      await client.login(
          auth_info_1=user_name,
          auth_info_2=EMAIL,
          password=pass_word
          #cookies_file='cookies.json'
      )
  
  asyncio.run(main())
  
  # ログイン情報を cookies.json に保存する
  #client.save_cookies("cookies.json")
  
