def UsersLookup(
  twitter_domain,ct0,auth_token,x_client_transaction_id,uid_query
):
  
  #import requests
  from curl_cffi import requests
  import json
  import CommonFunction
  
  url = "https://" + twitter_domain + "/i/api/1.1/users/lookup.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_is_blue_verified=1&include_ext_verified_type=1&include_ext_profile_image_shape=1&skip_status=1&user_id=" + uid_query
  
  headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'Cookie': 'auth_token=' + auth_token + '; ct0=' + ct0 + '; ',
    'x-client-transaction-id': x_client_transaction_id,
    'x-csrf-token': ct0,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    "content-type": "application/json",
    "method" : "GET",
    "accept" : "*/*",
    "accept-encoding" : "gzip, deflate, br, zstd",
    "accept-language" : "ja,en-US;q=0.9,en;q=0.8",
    'cache-control' : "no-cache",
    'Pragma' : "no-cache",
    'Priority' : "u=1, i",
    'Referer' : "https://" + twitter_domain + "/follower_requests",
    'Sec-ch-ua' : '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'Sec-ch-ua-Mobile' : "?0",
    'Sec-ch-ua-Platform' : '"Windows"',
    'Sec-fetch-Dest' : "empty",
    'Sec-fetch-Mode' : "cors",
    'Sec-fetch-Site' : "same-origin",
    'x-twitter-active-user' : "yes",
    'x-twitter-auth-type' : "OAuth2Session",
    'x-twitter-client-language' : "jp"
  }

  params ={
    #'muteHttpExceptions': 'true'
  }
  
  #リクエストパラメータチェック
  print('twitter_domain = ' + twitter_domain)
  print('uid_query = ' + uid_query)
  print('ct0 = ' + ct0)
  print('auth_token = ' + auth_token)
  print('x-client-transaction-id = ' + x_client_transaction_id)
  
  try:

    print("リクエストURL：" + url)
    
    # GETリクエストを送信
    response = requests.get(url, headers=headers)
  
    # レスポンスのステータスコードを表示
    print('ステータスコード:', response.status_code)

    #ステータスコードが200番台ではないのにexceptに飛んでくれないことがある、その対策
    #検知条件：ステータスコードを100で割ったときの商が2でない
    if response.status_code // 100 != 2:
      return {
        "code" : response.status_code,
        "message" : CommonFunction.Create_HTTPErrorMessage(response.status_code,response.text)
      }

    #レスポンスをjson形式に変換
    jsonData = response.json()
    
  except requests.exceptions.RequestException as e:
    #httpステータスコードが200番台でなかった場合、except句に流れる
    print("エラー : ",e)
    #エラーレスポンスを戻り値としてそのまま返却
    return e
  
  #レスポンスデータを戻り値としてそのまま返却
  return jsonData
