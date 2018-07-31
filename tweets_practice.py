import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter
from twitter import get_auth, twitter_api


auth = get_auth()

api = twitter_api()

#We'll create a user
user = api.get_user('GabyGuedezh')
followers = api.followers('GabyGuedezh')

#Then we access the screen_name and followers_count properties of the user object
# print("Screen Name:", user.screen_name)
# print("Followers:", user.followers_count)
# print("Following:", user.friends_count)
# print("Listed Count:", user.listed_count)
# print("Twitter Bio:", user.description)

user_dict = {
    "Screen Name:", user.screen_name,
    "Followers:", user.followers_count,
    "Following:", user.friends_count,
    "Listed Count", user.listed_count,
    "Twitter Bio", user.description
    }
            
print(user_dict)

# for follower in followers():
#     print(follower)

#My info in a table
#prettify
table = PrettyTable(field_names=['Screen Name', 'Followers', 'Following', 'Listed Count', 'Twitter Bio'])
    # counter = Counter(data)
table.add_row(user.screen_name)
print(table)   