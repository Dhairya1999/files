from kafka import KafkaProducer
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from transformers import pipeline
import json
import configparser


#Twitter API Authentication credentials
consumer_key = "QF5IPKz63N7jfUuuO8XxjlREP"
consumer_secret = "ObU6n4HQIAemLkRxrnXplXORHiQ75sdl4GDPsPPg3TggurEg13"
access_token = "1515508164896120835-juRiwVSPFaPHu7yfNQqeVkUNH0zTwJ"
access_secret = "53ldAbsxt2ToheGOndQ5kH1dK4SlIjVoxGJCnQKJe7tPr"


def perform_analysis(tweet):
	transformer_sentiment = classifier(json.loads(tweet)["text"])
	transformer_sentiment = transformer_sentiment[0]['label']
	return transformer_sentiment


class KafkaPushListener(StreamListener):
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])


    def on_data(self, data):
        transformer_sentiment = perform_analysis(data)
        self.producer.send("movie", transformer_sentiment.encode('utf-8'))
        return True

    def on_error(self, status):
        print("status error - ",status)
        return True



if __name__ == "__main__":
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)

    
	classifier = pipeline('sentiment-analysis')
	listener = KafkaPushListener()
	twitter_stream = Stream(auth, listener)

    
	twitter_stream.filter(track=['movie','mreviews'])
