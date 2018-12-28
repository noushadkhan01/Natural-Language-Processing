import string,re
import nltk
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('brown')
def clean_text(tweets, n = 0):
  tweets = word_tokenize(tweets)  #SEPERATE EACH WORD
  while True:
    try:
      a = tweets.index('@')
      del tweets[a + 1]
      tweets.remove('@')
    except:
      break
  while True:
    try:
      b = tweets.index('#')
      del tweets[b + 1]
      tweets.remove('#')
    except:
      break
  tweets = " ".join(tweets)#JOIN WORDS
  tweets = re.sub(r'http\S+', '', tweets)#REMOVE HTTPS TEXT WITH BLANK
  tweets = [char for char in tweets if char not in string.punctuation]#REMOVE PUNCTUATIONS
  tweets = ''.join(tweets)#JOIN THE LETTERS
  tweets = [word.lower() for word in tweets.split() if word.lower() not in stopwords.words('english')]#REMOVE COMMON ENGLISH WORDS(I,YOU,WE..
  return " ".join(tweets)
  
#get polarity
def get_polarity(tweet):
  from textblob import TextBlob
  tweet = TextBlob(tweet)
  pol = tweet.polarity
  return pol

def get_sentiment_analysis(df, freq_plot = False):
  import matplotlib.pyplot as plt
  from nltk.probability import FreqDist
  if freq_plot:
    user_list = df['screenName'].tolist()
    max_user = FreqDist(user_list)
    max_user.plot(10)
  df['cleaned_text']  = df['text'].apply(clean_text) #adding clean text to dataframe
  df['polarity'] = df['cleaned_text'].apply(get_polarity)
  
  print("THE AVERAGE POLARITY",np.mean(df["polarity"])) #gives the average sentiments of people
  print("THE MOST -VE TWEET :",df.iloc[df['polarity'].idxmin()][['created', 'text']])# most positive
  print("THE MOST +VE TWEET :",df.iloc[df['polarity'].idxmax()][['created', 'text']])#most negetive
  return df

  
