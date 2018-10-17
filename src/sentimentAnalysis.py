import tweepy
import numpy as np
from textblob import TextBlob
from settings import *

# Infelizmente a biblioteca textblob tá bugada
# e não conseguiremos utilizar o google tradutor
# para traduzir do inglês pro português :(

# Checa o idioma do tweet
"""
def is_english(text):
    if text.detect_language() == 'en':
        return True
    return False
"""

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

# Buscando tweets relacionados a python brasil ignorando retweets
tweets = api.search('Python Brasil -filter:retweets')

def tweet_analisys():
    polarities = []

    # Iterando os resultados e passando para o textblob
    for tweet in tweets:
        phrase = TextBlob(tweet.text)

        #if not is_english(phrase):
        #    phrase = TextBlob(str(phrase.translate(from_lang='pt', to='en')))

        if (phrase.sentiment.polarity != 0.0 and phrase.sentiment.subjectivity != 0.0):
            polarities.append(phrase.sentiment.polarity)


        print('Tweet: ' + tweet.text)
        print('Polarity: ' + str(phrase.sentiment.polarity) + " \ " + str(phrase.sentiment.subjectivity))
        print('.....................')

    return polarities

polarity_mean = np.mean(tweet_analisys())

print('Média: ' + str(polarity_mean))
if(polarity_mean > 0.0):
    print('POSITIVE')
else:
    print('NEGATIVE')
