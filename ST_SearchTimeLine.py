

def SearchTimeLine(
  twitter_domain,ct0,auth_token,x_client_transaction_id,query,cursor,max_count,T_L_Param
):
  import requests
  import json

  query_id = 'C1qZ6bs-L3oc_TKSZyxkXQ'

  #カーソルが送られなかった場合
  if cursor == 'undefined':
    cursor = ''
  
  url = "https://" + twitter_domain + "/i/api/graphql/AIdc203rPpK_k_2KWSdm7g/SearchTimeline?variables=%7B%22rawQuery%22%3A%22" + query + "22%2C%22count%22%3A" + max_count + "%2C" + cursor + "%22querySource%22%3A%22typed_query%22%2C%22product%22%3A%22" + T_L_Param + "%22%7D&features=%7B%22rweb_video_screen_enabled%22%3Afalse%2C%22profile_label_improvements_pcf_label_in_post_enabled%22%3Atrue%2C%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22premium_content_api_read_enabled%22%3Afalse%2C%22communities_web_enable_tweet_community_results_fetch%22%3Atrue%2C%22c9s_tweet_anatomy_moderator_badge_enabled%22%3Atrue%2C%22responsive_web_grok_analyze_button_fetch_trends_enabled%22%3Afalse%2C%22responsive_web_grok_analyze_post_followups_enabled%22%3Atrue%2C%22responsive_web_jetfuel_frame%22%3Afalse%2C%22responsive_web_grok_share_attachment_enabled%22%3Atrue%2C%22articles_preview_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22responsive_web_grok_show_grok_translated_post%22%3Afalse%2C%22responsive_web_grok_analysis_button_from_backend%22%3Atrue%2C%22creator_subscriptions_quote_tweet_preview_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_grok_image_annotation_enabled%22%3Atrue%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D"
  
  headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'Cookie': 'auth_token=' + auth_token + '; ct0=' + ct0 + '; ',
    'x-client-transaction-id': x_client_transaction_id,
    'x-csrf-token': ct0,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    "content-type": "application/json"
  }

  params ={
    #'muteHttpExceptions': 'true'
  }
  
  #リクエストパラメータチェック
  print('twitter_domain = ' + twitter_domain)
  print('ct0 = ' + ct0)
  print('auth_token = ' + auth_token)
  print('x-client-transaction-id = ' + x_client_transaction_id)
  print('cursor = ' + cursor)
  print('query = ' + query)
  print('max_count = ' + max_count)
  print('T_L_Param = ' + T_L_Param)
  
  try:
    # GETリクエストを送信
    response = requests.get(url, headers=headers,params=params)
  
    # レスポンスのステータスコードを表示
    print('ステータスコード:', response.status_code)

    #ステータスコードが200番台ではないのにexceptに飛んでくれないことがある、その対策
    #検知条件：ステータスコードを100で割ったときの商が2でない
    if response.status_code // 100 != 2:
      raise requests.exceptions.RequestException("Request Failed for Twitter API return code " + str(response.status_code))

    #レスポンスをjson形式に変換
    jsonData = response.json()
    
  except requests.exceptions.RequestException as e:
    #httpステータスコードが200番台でなかった場合、except句に流れる
    print("エラー : ",e)
    #エラーレスポンスを戻り値としてそのまま返却
    return e
  
  #レスポンスデータを戻り値としてそのまま返却
  return jsonData
