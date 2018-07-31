import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from twitter import get_auth, twitter_api


auth = get_auth()

api = twitter_api()

count = 5
query = 'jack russell'

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

# status_texts = [status._json['text'] for status in results]

screen_names = [ status._json['user']['screen_name']
                            for status in results
                                for mention in status._json['entities']['user_mentions'] ]

twitter_bio = [status._json['user']['description'] for status in results]                                
                                
# hashtags = [ hashtag['text'] for status in results
#                             for hashtag in status._json['entities']['hashtags'] ]

# words = [word for text in status_texts
#                 for word in text.split()]

location = [ status._json['user']['location'] for status in results]

# followers = [status._json['user']['followers_count'] for status in results]

verified = [status._json['user']['verified'] for status in results]

# for label, data in(('Text', status_texts),
#                     ('Screen Name', screen_names),
#                     ('Word', words)):
#     table = PrettyTable(field_names=[label, 'count'])
#     counter = Counter(data)
#     [table.add_row(entry) for entry in counter.most_common()[:10]]
#     print(table)

# for result in results:
#     print(json.dumps(result._json, indent=2))

# for status in results:
# #     print(status.text.encode('utf-8'))
# #     print(status.user.id)
#     print("screen_name: ", status.user.screen_name)
#     print("twitter_bio: ", status.user.description)
# #     print(status.user.profile_image_url_https)
# #     print(status.user.followers_count)
# #     print(status.place)
#     print("location: ", status.user.location)
#     print("followers: ", status.user.followers_count)
#     print('verified: ', status.user.verified)

for label, data in (('screen_name', screen_names),
                        ('twitter_bio', twitter_bio),
                        ('location', location),
                        ('verified', verified)):
    table = PrettyTable(field_names=[label, 'count'])
    counter = Counter(data)
    [table.add_row(entry) for entry in counter.most_common()[:5]]
    table.align[label], table.align['count'] = 'l', 'r'
    
    print(table)