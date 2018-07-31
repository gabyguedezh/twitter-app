import json
import tweepy
from tweepy import OAuthHandler
from twitter import get_auth, twitter_api


auth = get_auth()

api = twitter_api()

DUB_WOE_ID = 560743
LON_WOE_ID = 44418
BFT_WOE_ID = 44544
GLW_WOE_ID = 2450022

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)
bft_trends = api.trends_place(BFT_WOE_ID)
glw_trends = api.trends_place(GLW_WOE_ID)

dub_trends_set = set([trend['name']
                    for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                    for trend in lon_trends[0]['trends']])
                    
bft_trends_set = set([trend['name']
                    for trend in bft_trends[0]['trends']])                    

glw_trends_set = set([trend['name']
                    for trend in glw_trends[0]['trends']])                    
                    
common_trends = set.intersection(dub_trends_set, lon_trends_set)
common_trends_bft_glw = set.intersection(bft_trends_set, glw_trends_set)

common_trends_all = set.intersection(dub_trends_set, lon_trends_set, bft_trends_set, glw_trends_set)

print(common_trends_all)