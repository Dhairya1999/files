import tweepy

streaming_client = tweepy.StreamingClient("Bearer Token here")
streaming_client.add_rules(tweepy.StreamRule("Covid-19"))
streaming_client.filter()

class IDPrinter(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        print(tweet.id)


printer = IDPrinter("Bearer Token here")
printer.sample()
