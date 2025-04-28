from typing import Optional
from fastapi import FastAPI

import ST_TweetDetail

app = FastAPI()

import requests
import json

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/TweetDetail")
def read_item(
    twitter_domain,target_tweet_id,ct0,auth_token
):
    return ST_TweetDetail.TweetDetail(
        twitter_domain,target_tweet_id,ct0,auth_token
    )
