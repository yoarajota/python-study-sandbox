import tweepy
import config
import re

client = tweepy.Client(config.BEARER_TOKEN, config.API_KEY, config.API_SCRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

query = 'from:ioweasy -is:retweet'
response = client.search_recent_tweets(query=query)
            # o all é para a api premium ou academica algo assim

tweetId = response.data[0].id

query_replys_of_recent_tweet = 'from:yoarajota in_reply_to_tweet_id:{}'.format(tweetId)
replys_of_recent_tweet = client.search_recent_tweets(query=query_replys_of_recent_tweet).data

if (replys_of_recent_tweet is None):
    auth = tweepy.OAuth1UserHandler(config.API_KEY, config.API_SCRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    try_to_get_my_last_tweet_query = 'from:{}'.format(client.get_me().data.id)+' -is:retweet is:reply'
    last_tweet = client.search_recent_tweets(query=try_to_get_my_last_tweet_query).data[0]

    if (re.search('fodase', last_tweet.text)):
        #client.create_tweet(in_reply_to_tweet_id=tweetId, text='fodase')
        print('a')
    else:
        print('b')
        #client.create_tweet(in_reply_to_tweet_id=tweetId, text='nao pedi')
