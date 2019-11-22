import numpy as np
import pandas as pd
import re
import numpy as np
import pandas as pd
from pprint import pprint

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.parsing.preprocessing import STOPWORDS
from gensim.utils import simple_preprocess
from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamulticore import LdaMulticore

# Spacy for lemmatization
import spacy

# Plotting tools
import pyLDAvis
import pyLDAvis.gensim  # don't skip this
import matplotlib.pyplot as plt
%matplotlib inline

from textblob import TextBlob
import nltk
import nltk.data

from nltk import tokenize
from nltk.tokenize import sent_tokenize


df = pd.read_csv("comments.csv")

comment = df['text']

def tokenize(x):
    text = x.lower()
    test = x.re.sub(r'[^a-zA-Z ^0-9]', '', str(text))
    return test.split()

nltk.download('punkt')

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')


comment.isna().sum()

comment = comment.dropna()


sentiment_scores_tb = [round(TextBlob(article).sentiment.polarity, 3) for article in comment['text']]
sentiment_category_tb = ['positive' if score > 0 
                             else 'negative' if score < 0 
                                 else 'neutral' 
                                     for score in sentiment_scores_tb]








