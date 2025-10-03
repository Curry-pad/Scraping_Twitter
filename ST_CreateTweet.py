

def CreateTweet(
  twitter_domain,ct0,auth_token,x_client_transaction_id,tw_text,Reply_Avail_Setting,media_entities
):
  import requests
  import json
  import CommonFunction
  
  query_id = 'ZSBCfCefJFumbPcLcwR64Q'
  
  url = "https://" + twitter_domain + "/i/api/graphql/" + query_id + "/CreateTweet"

  options = {
    "variables": {
      "tweet_text": tw_text,
      "dark_request": False,
      "semantic_annotation_ids": [],
      "disallowed_reply_options": None
    },
    "features": {
      "premium_content_api_read_enabled": False,
      "communities_web_enable_tweet_community_results_fetch": True,
      "c9s_tweet_anatomy_moderator_badge_enabled": True,
      "responsive_web_grok_analyze_button_fetch_trends_enabled": False,
      "responsive_web_grok_analyze_post_followups_enabled": True,
      "responsive_web_jetfuel_frame": True,
      "responsive_web_grok_share_attachment_enabled": True,
      "responsive_web_edit_tweet_api_enabled": True,
      "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
      "view_counts_everywhere_api_enabled": True,
      "longform_notetweets_consumption_enabled": True,
      "responsive_web_twitter_article_tweet_consumption_enabled": True,
      "tweet_awards_web_tipping_enabled": False,
      "responsive_web_grok_show_grok_translated_post": False,
      "responsive_web_grok_analysis_button_from_backend": True,
      "creator_subscriptions_quote_tweet_preview_enabled": False,
      "longform_notetweets_rich_text_read_enabled": True,
      "longform_notetweets_inline_media_enabled": True,
      "payments_enabled": False,
      "profile_label_improvements_pcf_label_in_post_enabled": True,
      "rweb_tipjar_consumption_enabled": True,
      "verified_phone_label_enabled": False,
      "articles_preview_enabled": True,
      "responsive_web_grok_community_note_auto_translation_is_enabled": False,
      "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
      "freedom_of_speech_not_reach_fetch_enabled": True,
      "standardized_nudges_misinfo": True,
      "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
      "responsive_web_grok_image_annotation_enabled": True,
      "responsive_web_grok_imagine_annotation_enabled": True,
      "responsive_web_graphql_timeline_navigation_enabled": True,
      "responsive_web_enhance_cards_enabled": False
    },
    "queryId": query_id
  }
  
  headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'Cookie': 'auth_token=' + auth_token + '; ct0=' + ct0 + '; ',
    'x-client-transaction-id': x_client_transaction_id,
    'x-csrf-token': ct0,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    "content-type": "application/json"
  }

  #不要か？
  params ={
    #'muteHttpExceptions': 'True',
    "contentType": 'application/json',
    "payload" : options
  }
  
  #リクエストパラメータチェック
  print('twitter_domain = ' + twitter_domain)
  print('ct0 = ' + ct0)
  print('auth_token = ' + auth_token)
  print('x-client-transaction-id = ' + x_client_transaction_id)
  print('tw_text = ' + tw_text)
  print('Reply_Avail_Setting = ' + Reply_Avail_Setting)
  print('media_entities = ' + media_entities)
  
  try:
    
    print("リクエストURL：" + url)
    
    # GETリクエストを送信
    response = requests.post(url, headers=headers,json=options)
  
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
