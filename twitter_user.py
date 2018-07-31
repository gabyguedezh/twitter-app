import tweepy
from tweepy import OAuthHandler
from twitter import get_auth, twitter_api

auth = get_auth()

api = twitter_api()

#We'll create a user
user = api.get_user('@GabyGuedezh')
#The get_user returns a user instance that is assigned to the user variable

#Then we access the screen_name and followers_count properties of the user object
print(user.screen_name)
print(user.followers_count)

for friend in user.friends():
    print(friend.screen_name)
    print(friend.followers_count)

                

