from typing import Optional
from fastapi import FastAPI

#呼び出し先pyファイルたちを定義する
import CommonFunction
import ST_TweetDetail
import ST_Following
import ST_Followers
import ST_SearchTimeLine
import ST_QuoteTweet
import ST_UsersLookup
import ST_CreateTweet
import Twikit_Login
import Get_XClientTransactionId
import Get_XXpForwarded
import TweeterPy_Test
import PublicTwitterAPI_Tweet


app = FastAPI()

import requests
import json

@app.get("/")
async def root():
    print("実処理なし")
    #CommonFunction.Write_ExecuteLog("Test")
    return {
        "code" : 200,
        "message": "Hello World"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/TweetDetail")
def read_item(
    twitter_domain,ct0,auth_token,target_tweet_id
):
    return ST_TweetDetail.TweetDetail(
        twitter_domain,ct0,auth_token,target_tweet_id
    )

@app.get("/Following")
def read_item(
    twitter_domain,ct0,auth_token,guest_id,target_user_id,cursor
):
    return ST_Following.Following(
        twitter_domain,ct0,auth_token,guest_id,target_user_id,cursor
    )

@app.get("/Followers")
def read_item(
    twitter_domain,ct0,auth_token,guest_id,target_user_id,cursor
):
    return ST_Followers.Followers(
        twitter_domain,ct0,auth_token,guest_id,target_user_id,cursor
    )

@app.get("/SearchTimeLine")
def read_item(
    twitter_domain,ct0,auth_token,query,cursor,max_count,T_L_Param
):
    return ST_SearchTimeLine.SearchTimeLine(
        twitter_domain,ct0,auth_token,query,cursor,max_count,T_L_Param
    )

@app.get("/QuoteTweet")
def read_item(
    twitter_domain,ct0,auth_token,query,cursor,max_count,T_L_Param
):
    return ST_QuoteTweet.QuoteTweet(
        twitter_domain,ct0,auth_token,query,cursor,max_count,T_L_Param
    )

@app.get("/UsersLookup")
def read_item(
    twitter_domain,ct0,auth_token,uid_query
):
    return ST_UsersLookup.UsersLookup(
        twitter_domain,ct0,auth_token,uid_query
    )

@app.get("/CreateTweet")
def read_item(
    twitter_domain,ct0,auth_token,tw_text,Reply_Avail_Setting,media_entities
):
    return ST_CreateTweet.CreateTweet(
        twitter_domain,ct0,auth_token,tw_text,Reply_Avail_Setting,media_entities
    )

@app.get("/UserByRestId")
def read_item(
    twitter_domain,ct0,auth_token,query_id,features,user_agent,target_user_id
):
    return ST_UserByRestId.UserByRestId(
        twitter_domain,ct0,auth_token,query_id,features,user_agent,target_user_id
    )

@app.get("/Twikit_Login")
def read_item(
    user_name,EMAIL,password
):
    return Twikit_Login.Twikit_Login(
        user_name,EMAIL,password
    )

@app.get("/Get_XClientTransactionId")
def read_item(
    url,method
):
    return Get_XClientTransactionId.Get_XClientTransactionId(
        url,method
    )

@app.get("/Get_XXpForwarded")
def read_item(
    guest_id,user_agent
):
    return Get_XXpForwarded.Get_XXpForwarded(
        guest_id,user_agent
    )

@app.get("/TweeterPy_Test")
def read_item():
    return TweeterPy_Test.TweeterPy_Test()

@app.get("/PublicTwitterAPI_Tweet")
def read_item():
    return PublicTwitterAPI_Tweet.PublicTwitterAPI_Tweet()




