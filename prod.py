from kafka import KafkaProducer
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
#from tweepy.streaming import StreamListener
from transformers import pipeline
import json
import configparser


#Twitter API Authentication credentials
consumer_key = "GEBs5VLKwDan4oME4laUdMjGv"
consumer_secret = "OzIGA5lddzjdubebNGnHypn3KkNT2A6k2DXwCvKyHxb1lScpTP"
access_token = "855387525082427394-UeZaS4wsJ0Do4jhe7hTPzdwMhQI0NbX"
access_secret = "5laJDyt3lltmiTxL3MoNimWrdQivKrUQNzKo7MU5OxySc"
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAC07fQEAAAAAB7CyzHT8s1HfYB3lrrKa4rPx5P8%3DNnYqfBabqoI4nkGXAvIIgnsRa6JTtN89mnkdsaePieVAc9T5qy'


def perform_analysis(tweet):
	transformer_sentiment = classifier(json.loads(tweet)["text"])
	transformer_sentiment = transformer_sentiment[0]['label']
	return transformer_sentiment


class KafkaPushListener(tweepy.StreamingClient):
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])


    def on_data(self, data):
        transformer_sentiment = perform_analysis(data)
        self.producer.send("movie", transformer_sentiment.encode('utf-8'))
        return True

    def on_error(self, status):
        print("status error - ",status)
        return True

class IDPrinter(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        print(tweet.id)


if __name__ == "__main__":
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)

    
	classifier = pipeline('sentiment-analysis')
	listener = KafkaPushListener()
	streaming_client = tweepy.StreamingClient("AAAAAAAAAAAAAAAAAAAAAC07fQEAAAAAB7CyzHT8s1HfYB3lrrKa4rPx5P8%3DNnYqfBabqoI4nkGXAvIIgnsRa6JTtN89mnkdsaePieVAc9T5qy")
	streaming_client.add_rules(tweepy.StreamRule("Covid-19"))
	streaming_client.filter()
