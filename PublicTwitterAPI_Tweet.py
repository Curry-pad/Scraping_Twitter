
def PublicTwitterAPI_Tweet():

  print("PublicTwitterAPI_Tweet　はじめ")
  import os

  from curl_cffi import requests
  #import requests
  from requests_oauthlib import OAuth1

  print("認証情報取得　はじめ")
  
  # 環境変数から認証情報を取得
  api_key = os.getenv("OqxYkmu7PnTs6QQFljeu7fRZo")
  api_secret_key = os.getenv("a7QUOks1yW3iDO9OZG1WKCozDWS8j2fX4feLxPanrAGf8qM7Ae")
  access_token = os.getenv("1266022800071909377-OKjnTzl9dN6o84tlL3CJmwP5lJiiUs")
  access_token_secret = os.getenv("1YCEaUmh7CJxYeNXGODiC1bsFtlpEVxENTTUbA6VP75s0")

  print("認証情報セットできた")
  
  # OAuth 1.0a認証を設定
  auth_info = OAuth1(api_key, client_secret=api_secret_key, resource_owner_key=access_token, resource_owner_secret=access_token_secret)

  print(auth_info)
  
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

