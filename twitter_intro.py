import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'gujUWVtlofQXqvjb6NXh1YHIa'
CONSUMER_SECRET = 'TVzXFjFSmaphOBJiEflNJqYb2eYB6fx2I6LtYFhtpAGiLqA93j'
OAUTH_TOKEN = '37690003-fWlxS1GiHpzXB3yhL2MrMfXTMhLHAOqqJegzOPKV7'
OAUTH_TOKEN_SECRET = 'pUlDp3NlQqVzzXPuCNLqrI3xIuaQt8aPcyw6op0t0Aanz'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

DUB_WOE_ID = 560743

dub_trends = api.trends_place(DUB_WOE_ID)

print(json.dumps(dub_trends, indent=1))