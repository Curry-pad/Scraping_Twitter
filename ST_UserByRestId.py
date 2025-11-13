def UserByRestId(
  twitter_domain,ct0,auth_token,query_id,features,user_agent,target_user_id
):
  
  #import requests
  from curl_cffi import requests
  import json
  import CommonFunction
  import Get_XClientTransactionId
  
  url = "https://api." + twitter_domain + "/graphql/" + query_id + "/UserByRestId?variables=%7B%22userId%22%3A%22" + target_user_id + "%22%7D&features=" + features

  #XCTIを生成する。これがうまくいけば、引数のXCTIは不要になる
  xcti_res = Get_XClientTransactionId.Get_XClientTransactionId(
    url,"GET"
  )
  #XPFFも取得する。
  xpff_res = Get_XXpForwarded.Get_XXpForwarded(
    guest_id,user_agent
  )
  
  headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    "method": "GET",
    "authority": "api." + twitter_domain,
    "path": "/graphql/" + query_id + "/UserByRestId?variables=%7B%22userId%22%3A%22" + target_user_id + "%22%7D&features=" + features,
    "scheme": "https",
    "content-type": "application/json",
    "accept": "*/*",
    "sec-fetch-site": "same-site",
    "x-twitter-client-language": "ja",
    "sec-fetch-mode": "cors",
    "origin": "https://" + twitter_domain,
    "user-agent": user_agent,
    "referer": "https://" + twitter_domain + "/",
    "x-xp-forwarded-for": xpff_res["Encrypted"],
    "sec-fetch-dest": "empty",
    "x-twitter-active-user": "yes",
    "accept-language": "ja",
    "priority": "u=3, i",
    "accept-encoding": "gzip, deflate, br",
    "cookie": 'auth_token=' + auth_token + '; ct0=' + ct0 + '; ',
    'x-client-transaction-id' : xcti_res["created_XCTI"],
    'x-csrf-token': ct0
  }

  params ={
    #'muteHttpExceptions': 'true'
  }
  
  #リクエストパラメータチェック,,
  print('twitter_domain = ' + twitter_domain)
  print('ct0 = ' + ct0)
  print('auth_token = ' + auth_token)
  print('features = ' + features)
  print('user_agent = ' + user_agent)
  print('query_id = ' + query_id)
  print('target_user_id = ' + target_user_id)
  print('x-client-transaction-id = ' + xcti_res["created_XCTI"])
  print('x-xp-forwarded-for = ' + xpff_res["Encrypted"])
  
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
