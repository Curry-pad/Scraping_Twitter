
def PublicTwitterAPI_Tweet():

  import os
  import requests
  from requests_oauthlib import OAuth1
  
  # 環境変数から認証情報を取得
  api_key = os.getenv("API_KEY")
  api_secret_key = os.getenv("API_SECRET_KEY")
  access_token = os.getenv("ACCESS_TOKEN")
  access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
  
  # OAuth 1.0a認証を設定
  auth = OAuth1(api_key, api_secret_key, access_token, access_token_secret)
  
  # ツイート内容の設定
  tweet_content = "Hello from OAuth 1.0a! This is an automated tweet."
  
  # APIエンドポイント
  url = "https://api.twitter.com/2/tweets"
  
  # リクエストペイロード
  payload = {"text": tweet_content}
  
  # POSTリクエストを送信
  response = requests.post(url, auth=auth, json=payload)
  
  # 結果を確認
  if response.status_code == 201:
      print("Successfully posted to Twitter!")
  else:
      print(f"Failed to post to Twitter: {response.status_code}")
      print(response.json())

