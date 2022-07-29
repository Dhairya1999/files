import tweepy

streaming_client = tweepy.StreamingClient("AAAAAAAAAAAAAAAAAAAAAC07fQEAAAAAB7CyzHT8s1HfYB3lrrKa4rPx5P8%3DNnYqfBabqoI4nkGXAvIIgnsRa6JTtN89mnkdsaePieVAc9T5qy")
streaming_client.add_rules(tweepy.StreamRule("Covid-19"))
streaming_client.filter()

class IDPrinter(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        print(tweet.id)


printer = IDPrinter("AAAAAAAAAAAAAAAAAAAAAC07fQEAAAAAB7CyzHT8s1HfYB3lrrKa4rPx5P8%3DNnYqfBabqoI4nkGXAvIIgnsRa6JTtN89mnkdsaePieVAc9T5qy")
printer.sample()
