"""
    Los top 10 tweets más retweeted.
    Los top 10 usuarios en función de la cantidad de tweets que emitieron.
    Los top 10 días donde hay más tweets.
    Los top 10 hashtags más usados.
"""
import json

def tweets_most_retweeted():
    with open('farmers-protest-tweets-2021-03-5.json') as data_file:
        tweets = []
        for i in range(1000):
            data = json.loads(data_file.readline())
            tweets.append((data['url'], data['retweetCount']))
        tweets = sorted(tweets, key=lambda retweets: retweets[1])
        for i in range(999, 989, -1):
            print(tweets[i])

def users_most_tweets():
    with open('farmers-protest-tweets-2021-03-5.json') as data_file:
        tweets = []
        for i in range(1000):
            data = json.loads(data_file.readline())
            tweets.append((data['user']['username'], data['user']['mediaCount']))
        tweets = sorted(tweets, key=lambda retweets: retweets[1])
        for i in range(999, 989, -1):
            print(tweets[i])

def days_most_tweets():
    with open('farmers-protest-tweets-2021-03-5.json') as data_file:
        tweets = {}
        for i in range(100000):
            data = json.loads(data_file.readline())
            if data['date'] not in tweets.keys():
                tweets[data['date'].split('T')[0]] =  1
            else:
                tweets[data['date'].split('T')[0]] +=  1
        tweets2 = []
        for k, v in tweets.items():
            tweets2.append((k, v))
        tweets2 = sorted(tweets2, key=lambda retweets: retweets[1])
        for i in range(10):
            print(tweets2[i])

def hashtags_most_used():
    pass

if __name__=="__main__":
    users_most_tweets()