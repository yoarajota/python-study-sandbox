import tweepy
import config

client = tweepy.Client(config.BEARER_TOKEN, config.API_KEY, config.API_SCRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

query = 'from:Z3N0n_ -is:retweet'
response = client.search_recent_tweets(query=query)
            # o all é para a api premium ou academica algo assim

tweetId = response.data[0].id

auth = tweepy.OAuth1UserHandler(config.API_KEY, config.API_SCRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

client.create_tweet(in_reply_to_tweet_id=tweetId, text='fodaseeeeeeee')