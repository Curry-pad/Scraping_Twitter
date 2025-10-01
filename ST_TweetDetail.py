# -*- coding: utf-8 -*-

def TweetDetail(
  twitter_domain,ct0,auth_token,x_client_transaction_id,target_tweet_id
):
  import requests
  import json
  import CommonFunction
  import chardet
  
  #query_id = "_8aYOgEDz35BrBcBal1-_w"
  #2025/05/04　クエリID変更対応
  #query_id = "c9RRUtQyVCoDVtyu4CXG0g"
  #2025/05/06　またクエリIDが変わった…。
  #query_id = "xd_EMdYvB9hfZsZ6Idri0w"
  #2025/07/19  またかい…クエリID変更対応
  #query_id = "aTYmkYpjWyvUyrinVWSiYA"
  #2025/09/30　クエリID変更対応
  query_id = "JgryuItLZQ9V56vHjGIWWw"
  
  #ツイートID以降のクエリ文字列。定期的に変更されることがあるので、ここででふぁいん切っておく
  #query_str = "%22%2C%22referrer%22%3A%22profile%22%2C%22controller_data%22%3A%22DAACDAABDAABCgABAAAAAAAAAAAKAAkUx7wEslqQAgAAAAA%3D%22%2C%22with_rux_injections%22%3Afalse%2C%22rankingMode%22%3A%22Relevance%22%2C%22includePromotedContent%22%3Atrue%2C%22withCommunity%22%3Atrue%2C%22withQuickPromoteEligibilityTweetFields%22%3Atrue%2C%22withBirdwatchNotes%22%3Atrue%2C%22withVoice%22%3Atrue%7D&features=%7B%22rweb_video_screen_enabled%22%3Afalse%2C%22payments_enabled%22%3Afalse%2C%22profile_label_improvements_pcf_label_in_post_enabled%22%3Atrue%2C%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22premium_content_api_read_enabled%22%3Afalse%2C%22communities_web_enable_tweet_community_results_fetch%22%3Atrue%2C%22c9s_tweet_anatomy_moderator_badge_enabled%22%3Atrue%2C%22responsive_web_grok_analyze_button_fetch_trends_enabled%22%3Afalse%2C%22responsive_web_grok_analyze_post_followups_enabled%22%3Atrue%2C%22responsive_web_jetfuel_frame%22%3Atrue%2C%22responsive_web_grok_share_attachment_enabled%22%3Atrue%2C%22articles_preview_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22responsive_web_grok_show_grok_translated_post%22%3Afalse%2C%22responsive_web_grok_analysis_button_from_backend%22%3Afalse%2C%22creator_subscriptions_quote_tweet_preview_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_grok_image_annotation_enabled%22%3Atrue%2C%22responsive_web_grok_community_note_auto_translation_is_enabled%22%3Afalse%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D&fieldToggles=%7B%22withArticleRichContentState%22%3Atrue%2C%22withArticlePlainText%22%3Afalse%2C%22withGrokAnalyze%22%3Afalse%2C%22withDisallowedReplyControls%22%3Afalse%7D"
  #2025/09/30　更新
  query_str = "%22%2C%22referrer%22%3A%22me%22%2C%22with_rux_injections%22%3Afalse%2C%22rankingMode%22%3A%22Relevance%22%2C%22includePromotedContent%22%3Atrue%2C%22withCommunity%22%3Atrue%2C%22withQuickPromoteEligibilityTweetFields%22%3Atrue%2C%22withBirdwatchNotes%22%3Atrue%2C%22withVoice%22%3Atrue%7D&features=%7B%22rweb_video_screen_enabled%22%3Afalse%2C%22payments_enabled%22%3Afalse%2C%22profile_label_improvements_pcf_label_in_post_enabled%22%3Atrue%2C%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22premium_content_api_read_enabled%22%3Afalse%2C%22communities_web_enable_tweet_community_results_fetch%22%3Atrue%2C%22c9s_tweet_anatomy_moderator_badge_enabled%22%3Atrue%2C%22responsive_web_grok_analyze_button_fetch_trends_enabled%22%3Afalse%2C%22responsive_web_grok_analyze_post_followups_enabled%22%3Atrue%2C%22responsive_web_jetfuel_frame%22%3Atrue%2C%22responsive_web_grok_share_attachment_enabled%22%3Atrue%2C%22articles_preview_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22responsive_web_grok_show_grok_translated_post%22%3Afalse%2C%22responsive_web_grok_analysis_button_from_backend%22%3Atrue%2C%22creator_subscriptions_quote_tweet_preview_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_grok_image_annotation_enabled%22%3Atrue%2C%22responsive_web_grok_imagine_annotation_enabled%22%3Atrue%2C%22responsive_web_grok_community_note_auto_translation_is_enabled%22%3Afalse%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D&fieldToggles=%7B%22withArticleRichContentState%22%3Atrue%2C%22withArticlePlainText%22%3Afalse%2C%22withGrokAnalyze%22%3Afalse%2C%22withDisallowedReplyControls%22%3Afalse%7D"
  
  url = 'https://' + twitter_domain + '/i/api/graphql/' + query_id + '/TweetDetail?variables=%7B%22focalTweetId%22%3A%22' + target_tweet_id + query_str
  
  headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'Cookie': 'auth_token=' + auth_token + '; ct0=' + ct0 + '; ',
    'x-client-transaction-id': x_client_transaction_id,
    'x-csrf-token': ct0,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    "content-type": "application/json",
    #"content-type": "application/x-www-form-urlencoded",
    "method" : "GET",
    "accept" : "*/*",
    "accept-encoding" : "gzip, deflate, br",
    "accept-language" : "ja,en-US;q=0.9,en;q=0.8",
    'cache-control' : "no-cache",
    'Pragma' : "no-cache",
    'Priority' : "u=1, i",
    'referer' : "https://" + twitter_domain + "/i/status/" + target_tweet_id,
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
  print('target_tweet_id = ' + target_tweet_id)
  print('ct0 = ' + ct0)
  print('auth_token = ' + auth_token)
  print('x-client-transaction-id = ' + x_client_transaction_id)
  
  try:

    print("リクエストURL：" + url)
    
    # GETリクエストを送信
    response = requests.get(url, headers=headers)
    
    print('レスポンスヘッダー：',response.headers)
    print('バイナリデータ：',response.content)

    print('文字コード（修正前）：', response.encoding)

    #自動検出したエンコード
    a_encoding = response.apparent_encoding

    #エンコードの自動検出に失敗した場合は、無理やり文字コードを設定。何にすればよいのか…。
    if a_encoding == None:
      print('エンコード自動検出失敗')
      response.encoding = 'utf-8'
    else:
      print('エンコード自動検出成功')
      response.encoding = a_encoding
    
    print('文字コード（修正後）：', response.encoding)
  
    # レスポンスのステータスコードを表示
    print('ステータスコード:', response.status_code)
    print(response.text)

    #ステータスコードが200番台ではないのにexceptに飛んでくれないことがある、その対策
    #検知条件：ステータスコードを100で割ったときの商が2でない
    if response.status_code // 100 != 2:
      return {
        "code" : response.status_code,
        "message" : CommonFunction.Create_HTTPErrorMessage(response.status_code,response.text)
      }

    #レスポンスをjson形式に変換
    jsonData = response.json(ensure_ascii=False)
    
  except requests.exceptions.RequestException as e:
    #httpステータスコードが200番台でなかった場合、except句に流れる
    print("エラー : ",e)
    #エラーレスポンスを戻り値としてそのまま返却
    return e
  
  #レスポンスデータを戻り値としてそのまま返却
  return jsonData
