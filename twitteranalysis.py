import tweepy
from textblob import TextBlob
import pandas

consumer_key = 'mStlWz5wFnNywpeij9vd22qrC'
consumer_secret = 'LbfZoS1M9vt11sf9QDk7Su7CFBvFkxH5UyAhoBeFL8PDKFXlEV'

access_token = "1068824794798284800-OU4Tpge2Xxxuq0WNkd5kRIY2hJP4sY"
access_token_secret = 'p9xI7TIZ4SYXSAYf1OMZwQa1258Kpge5b2O0vkW9lPsDE'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Australia')

fname = 'tweets.csv'

def calc(a):
    if a < 0.2: 
        return 'negative \n'
    else:
        return 'positive \n'

f = open(fname,'w')

for tweet in public_tweets[0:100]:
    analysis = TextBlob(tweet.text)
    string = tweet.text + ' , '+ calc(analysis.sentiment.polarity) 
    f.write(string)
    
    