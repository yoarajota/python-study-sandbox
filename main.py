import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query2 = 'malphite'
response = client.search_recent_tweets(query=query)
            # o all é para a api premium ou academica algo assim

for t in response.data:
    print(t)
