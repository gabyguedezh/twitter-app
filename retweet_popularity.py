import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter
from twitter import get_auth, twitter_api


auth = get_auth()

api = twitter_api()

count = 150
query = 'Ireland'

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 10 #the min amount of times a status is retweeted to gain entry to our list

#Loop through the results and check that retweet#-count is greater than the threshold
pop_tweets = [status for status in results 
                if status._json['retweet_count'] > min_retweets]

#Now create a list of tuples associating tweets' texts with their retweet_count
tweet_tups = [(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count'])
                for tweet in pop_tweets]
                
#Sort the tuple's entries in descending order
most_popular_tups = sorted(tweet_tups, key=itemgetter(1), reverse=True)[:5]

#prettify
table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in most_popular_tups:
    table.add_row([key, val])
    table.max_width['Text'] = 50
    table.align['Text'], table.align['Retweet Count'] = 'l', 'r'
print(table)
                

