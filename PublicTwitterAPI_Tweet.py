
def PublicTwitterAPI_Tweet():

  print("PublicTwitterAPI_Tweet　はじめ")
  import os

  from curl_cffi import requests
  #import requests
  #from requests_oauthlib import OAuth1Session
  from requests_oauthlib import OAuth2Session

  print("認証情報取得　はじめ")

  REDIRECT_URI = "https://twitter.com/";
  AUTHORIZATION_BASE_URL = "https://twitter.com/i/oauth2/authorize"
  TOKEN_URL = "https://api.twitter.com/2/oauth2/token"
  
  # 環境変数から認証情報を取得
  api_key = os.getenv("OqxYkmu7PnTs6QQFljeu7fRZo")
  api_secret_key = os.getenv("a7QUOks1yW3iDO9OZG1WKCozDWS8j2fX4feLxPanrAGf8qM7Ae")
  access_token = os.getenv("1266022800071909377-OKjnTzl9dN6o84tlL3CJmwP5lJiiUs")
  access_token_secret = os.getenv("1YCEaUmh7CJxYeNXGODiC1bsFtlpEVxENTTUbA6VP75s0")
  CLIENT_ID = "Xzh2ejZVeFI2WDZWdERYUkRDMG46MTpjaQ"
  CLIENT_SECRET = "AdAWmqd736SjI0I3KuizsTRkISLs7aN8Luko-tAdXOPHJJMvjy"

  print("認証情報セットできた")
  
  # OAuth 1.0a認証を設定
  #auth_info = OAuth1Session(api_key, client_secret=api_secret_key, resource_owner_key=access_token, resource_owner_secret=access_token_secret)

  # Step 1: Create an OAuth2 session
  twitter = OAuth2Session(
      client_id=CLIENT_ID,
      redirect_uri=REDIRECT_URI,
      scope=["tweet.read", "users.read", "offline.access"]  # Adjust scopes as needed
  )
  
  #print(auth_info)
  print(twitter)

  authorization_url, state = twitter.authorization_url(AUTHORIZATION_BASE_URL)
  print(f"Visit this URL to authorize: {authorization_url}")

  #return
  
  # ツイート内容の設定
  tweet_content = "Hello from OAuth 1.0a! This is an automated tweet."
  
  # APIエンドポイント
  url = "https://api.twitter.com/2/tweets"
  
  # リクエストペイロード
  payload = {"text": tweet_content}

  print("リクエスト開始")
  
  # POSTリクエストを送信
  response = requests.post(url, auth=auth_info, json=payload)

  print("リクエストできた")
  
  # 結果を確認
  if response.status_code == 201:
      print("Successfully posted to Twitter!")
  else:
      print(f"Failed to post to Twitter: {response.status_code}")
      print(response.json())

