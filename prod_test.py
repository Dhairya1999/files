import tweepy
from transformers import pipeline
import json
import configparser

def perform_analysis(text):
	transformer_sentiment = classifier(text)
	transformer_sentiment = transformer_sentiment[0]['label']
	return transformer_sentiment

class IDPrinter(tweepy.StreamingClient):
    def _init_(self):
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def on_tweet(self, tweet):
        a=perform_analysis(tweet.text)
        self.producer.send("tp1", a.encode('utf-8'))
        
        
classifier = pipeline('sentiment-analysis')
printers = IDPrinter("AAAAAAAAAAAAAAAAAAAAAC07fQEAAAAAB7CyzHT8s1HfYB3lrrKa4rPx5P8%3DNnYqfBabqoI4nkGXAvIIgnsRa6JTtN89mnkdsaePieVAc9T5qy")
printers.add_rules(tweepy.StreamRule("Covid-19"))
printers.filter()
