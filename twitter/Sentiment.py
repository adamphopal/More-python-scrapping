import tweepy
from textblob import TextBlob

consumer_key = 'K6VmuHewqBjxDp3IAp18MZqiX'
consumer_secret = 'VrQHA0MS2mJFsouGgStNyUnqvt1L9YtR6UVdA7PVkPD7Ywhgqd'

access_token = '936623210501619713-LgvjALs0n8Ib6XsbmR2PZ5uQrqxyhU1'
access_token_secret = 'g1fX4SuXHsnI0SYMRmVrh5FcMHc4XwEoYyR4BY3BvzHmM'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")