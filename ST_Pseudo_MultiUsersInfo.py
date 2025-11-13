#なんちゃって（疑似的）複数人ユーザ情報取得
#403エラーになって使えなくなってしまった複数人ユーザ情報取得(users/lookup)に代わり、UserByRestIdで疑似的にそれを実現する。
def Pseudo_MultiUsersInfo(
  twitter_domain,ct0,auth_token,query_id,features,guest_id,user_agent,target_uid_query
):

  import ST_UserByRestId

  #target_uid_queryは、カンマ区切りになったユーザID文字列を渡してもらう想定。
  #そのため、ここでカンマで区切って配列にする
  #https://www.kikagaku.co.jp/kikagaku-blog/python-split/#i-1
  target_uid_array = target_uid_query.split(',')

  #戻り値返却用
  uinfo_array = []
  
  #forでまわす
  for target_user_id in target_uid_array:

    tmp_uinfo = ST_UserByRestId.UserByRestId(
      twitter_domain,ct0,auth_token,query_id,features,guest_id,user_agent,target_user_id
    )

    print(tmp_uinfo)
    
    #データに欠けがある場合はスキップ
    if(tmp_uinfo is None):
      print('データに欠けがあります(tmp_uinfo)。')
      continue

    if(tmp_uinfo["data"] is None):
      print('データに欠けがあります(data)。')
      continue

    if(tmp_uinfo["data"]["user"] is None):
      print('データに欠けがあります(user)。')
      continue

    if(tmp_uinfo["data"]["user"]["result"] is None):
      print('データに欠けがあります(result)。')
      continue
    
    #https://note.nkmk.me/python-list-append-extend-insert/
    uinfo_array.append(
      tmp_uinfo["data"]["user"]["result"]
    )
  
  
  return uinfo_array
