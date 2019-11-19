# Define a function to return the sentiment score of a comment
from textblob import TextBlob

def sentiment_score(comment):
    score = round(TextBlob(comment).sentiment.polarity, 3) 
    # the more negative the ouput value the, the more negative the sentiment of the comment
    return score


# Query HackerNews dataset for top contributors
def name_lister(df, cutoff): #df should contain by and comments features
    # query for only those commenters with at least 100 comments
    df2 = pd.DataFrame(df.by.value_counts()).reset_index()
    df2 = df2[df2.by >= cutoff]  # cutoff is minimum number of comments 
    df2 = df2.rename(columns={'index': 'by', 'by': 'amount'})
    names_list = df2.by
    return names_list


# Define a function to return a dataset of most frequent commenters and their 
#  respective aggregate saltiness 
def salt_scorer(names_list, df): 
    salt_list = []
    df = df[['text', 'by']].dropna()
    for name in names_list:
        comments_list = (df[df.by == name].reset_index()).text
        score_list = []
        for comment in comments_list:
            score = round(TextBlob(comment).sentiment.polarity, 3)
            score_list.append(score)
        saltiness = sum(score_list)/len(score_list)
        salt_list.append(saltiness)
    name_scores = pd.DataFrame(list(zip(names_list, salt_list)), columns = ['name', 'saltiness'])
    return name_scores


# Rank commenters based on their respective aggregate saltiness
def ranker(df):
    df = df.sort_values(by='saltiness') # lower values equate to higher saltiness
    df['rank'] = df['saltiness'].rank()
    return df


# Run an example using above crafted functions
# ranker(salt_scorer(name_lister(df, 500), df))