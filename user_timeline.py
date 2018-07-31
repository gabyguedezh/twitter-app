import tweepy
from tweepy import OAuthHandler
from twitter import get_auth, twitter_api


auth = get_auth()

api = twitter_api()

for status in tweepy.Cursor(api.home_timeline).items(10):
    #Process a tweet
    print(status.text)

