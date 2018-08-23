import tweepy
import os
from textblob import TextBlob

consumer_key = 'pQMhUUaT0NJF0yRDb61atIwnD'
consumer_secret = 'arm8xMnprRRjQakQQ24ZbVxFU9SDyZwwpSLTApfKOVinC22uCz'
access_token = '4833535092-9WhJXNalIkapipdEfUp24vxCoO3BGUm9OiMpjTT'
access_token_secret = 'r56d7hywUUvVFPPx8pmkLTsUfEkWERfgBHBVlUVckds0J'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

keys = raw_input("Enter search term: ")
public_tweets = api.search(keys)

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
print(os.getcwd())