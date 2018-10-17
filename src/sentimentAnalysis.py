import tweepy
import numpy as np
from textblob import TextBlob
from settings import *

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

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

def tweet_analisys(query):
    tweets = tweepy.Cursor(api.search, q=query + " -filter:retweets").items(20)

    polarities = []
    subjectivities = []

    # Iterando os resultados e passando para o textblob
    for tweet in tweets:
        phrase = TextBlob(tweet.text)

        #if not is_english(phrase):
        #    phrase = TextBlob(str(phrase.translate(from_lang='pt', to='en')))

        if (phrase.sentiment.polarity != 0.0 and phrase.sentiment.subjectivity != 0.0):
            polarities.append(phrase.sentiment.polarity)
            subjectivities.append(phrase.sentiment.subjectivity)

        """
        print('Tweet: ' + tweet.text)
        print('Polarity: ' + str(phrase.sentiment.polarity) + " \ " + str(phrase.sentiment.subjectivity))
        print('.....................')
        """
        
    return {'polarity':polarities, 'subjectivity':subjectivities}

# Utiliza uma media ponderada da polaridade utilizando a subjetividade como peso
# textos subjetivos (com mais emoção) terão peso maior
def get_weighted_polarity_mean(valid_tweets):
    return np.average(valid_tweets['polarity'],weights=valid_tweets['subjectivity'])

def get_polarity_mean(valid_tweets):
    return np.mean(valid_tweets['polarity'])

def print_result(mean):
    if mean > 0.0:
        print('POSITIVE')
    elif mean == 0.0:
        print('NEUTRO')
    else:
        print('NEGATIVE')

if __name__ == "__main__":
    query = input("Entre a query de analise: ")
    analysis = tweet_analisys(query)

    print('MÉDIA PONDERADA: ' + str(get_weighted_polarity_mean(analysis)))
    print_result(get_weighted_polarity_mean(analysis))

    print('MÉDIA: ' + str(get_polarity_mean(analysis)))
    print_result(get_polarity_mean(analysis))
