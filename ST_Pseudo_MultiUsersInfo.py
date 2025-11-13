def Pseudo_MultiUsersInfo(
  twitter_domain,ct0,auth_token,query_id,features,guest_id,user_agent,target_uid_query
):

  import ST_UserByRestId

  #target_uid_queryは、カンマ区切りになったユーザID文字列を渡してもらう想定。
  #そのため、ここでカンマで区切って配列にする
  #https://www.kikagaku.co.jp/kikagaku-blog/python-split/#i-1
  target_uid_array = target_uid_query.split(',')
  
  #forでまわす
  

  
  #twitter_domain,ct0,auth_token,query_id,features,guest_id,user_agent,target_user_id
