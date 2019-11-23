from textblob import TextBlob
import numpy as np
import pandas as pd

# file is 3GB
df = pd.read_csv("comments.csv")

comment = df

comment.isna().sum()

comment = comment.dropna()

print('This could take a while, go grab a cup of coffe')
sentiment_scores_tb = [round(TextBlob(article).sentiment.polarity, 3) for article in comment['text']]
print('Done !!!!')

comment['feels'] = sentiment_scores_tb

top100 = comment.sort_values(by=['feels']).head(100)

top100 = top100.drop(['feels'], axis=1)

print('Exporting CSV file')
top100.to_csv('top100_comments.csv')

print('Exporting JSON file')
top100.to_json(orient='columns',path_or_buf='top_100_comments.json')