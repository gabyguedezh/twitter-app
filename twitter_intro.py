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
LON_WOE_ID = 44418

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

dub_trends_set = set([trend['name']
                    for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                    for trend in lon_trends[0]['trends']])
                    
common_trends = set.intersection(dub_trends_set, lon_trends_set)

print(common_trends)