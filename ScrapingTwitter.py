from typing import Optional
from fastapi import FastAPI

import ST_TweetDetail

app = FastAPI()

import requests
import json

@app.get("/")
async def root():
    print("実処理なし")
    return {
        "code" : 200,
        "message": "Hello World"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/TweetDetail")
def read_item(
    twitter_domain,ct0,auth_token,x_client_transaction_id,target_tweet_id
):
    return ST_TweetDetail.TweetDetail(
        twitter_domain,ct0,auth_token,x_client_transaction_id,target_tweet_id
    )

@app.get("/Following")
def read_item(
    twitter_domain,ct0,auth_token,x_client_transaction_id,target_user_id,cursor
):
    return ST_Following.Following(
        twitter_domain,ct0,auth_token,x_client_transaction_id,target_user_id,cursor
    )

@app.get("/Followers")
def read_item(
    twitter_domain,ct0,auth_token,x_client_transaction_id,target_user_id,cursor
):
    return ST_Followers.Followers(
        twitter_domain,ct0,auth_token,x_client_transaction_id,target_user_id,cursor
    )

@app.get("/SearchTimeLine")
def read_item(
    twitter_domain,ct0,auth_token,x_client_transaction_id,query,cursor,max_count
):
    return ST_SearchTimeLine.SearchTimeLine(
        twitter_domain,ct0,auth_token,x_client_transaction_id,query,cursor,max_count
    )

