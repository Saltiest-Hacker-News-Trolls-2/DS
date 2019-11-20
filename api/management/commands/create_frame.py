from django.core.management.base import BaseCommand, CommandError
from textblob import TextBlob
import pandas as pd
from django_pandas.io import read_frame
from api.models import Items, SaltyUser
import requests as requests 

"""
BE CAREFUL WITH THESE COMMANDS
It takes a while for these functions to complete and 
populate the database. When running the command the previous database 
will be deleted
"""
class Command(BaseCommand):
    def handle(self, *args, **options):
        print("deleting objects in database")
        SaltyUser.objects.all().delete()
        print('done')

        print("querying items and running algorithm")
        qs = Items.objects.all()
        df = read_frame(qs)
        df.to_json(orient="split")
        # print(df)


        def sentiment_score(comment):
            score = round(TextBlob(comment).sentiment.polarity, 3) 
            # the more negative the ouput value the, the more negative the sentiment of the comment
            return score


        # Query HackerNews dataset for top contributors
        def name_lister(df, cutoff): #df should contain by and comments features
            # query for only those commenters with at least 100 comments
            df2 = pd.DataFrame(df.by.value_counts()).reset_index()
            df2 = df2[df2.by >= cutoff]  # cutoff is minimum number of comments per user
            df2 = df2.rename(columns={'index': 'by', 'by': 'amount'})
            names_list = df2.by
            return names_list


        # Define a function to return hackers'
        #  respective aggregate saltiness ranks
        def salt_scorer_mk1(names_list, df): 
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
            name_scores = pd.DataFrame(list(zip(names_list, salt_list)), columns = ['name', 'hacker_salt_score'])
            return name_scores


        # Rank commenters based on their respective aggregate saltiness
        def ranker(df):
            df = df.sort_values(by='hacker_salt_score') # lower values equate to higher saltiness
            df['rank'] = df['hacker_salt_score'].rank()
            return df #a dataset including ranks of hackers 


        # Define a function to return a comprehensive tiddy dataset
        def salt_scorer_mk2(df, ranked_df):
            # to get ranked_df: ranker(salt_scorer_mk1(name_lister(df, cutoff), df))
            
            df = df[['id','text', 'by']].dropna() 
            # TODO Generate data for an additional 4 features: 
            #  user_rank, comment_saltiness, user_comment_rank, sarcasm
            
            hacker_list = ranked_df.name
            hacker_rank = 1
            
            #prep a table for storage
            full_table = pd.DataFrame(columns = ['id', 'hacker', 'hacker_salt_ranking',
                                            'comment', 'comment_saltiness_score'])
                                                #,'hacker_specific_comment_rank'])
            
            for i in hacker_list:
                comment_list = (df[df.by == i].reset_index()).text
                id_list = (df[df.by == i].reset_index()).id
                name_list = (df[df.by == i].reset_index()).by
                
                comment_salt_score_list = []
                hacker_salt_rank_list = []
                #hacker_specific_comment_rank_list = []
                
                for comment in comment_list:
                    score = round(TextBlob(comment).sentiment.polarity, 3)
                    comment_salt_score_list.append(score)
                    
                    hacker_salt_rank_list.append(hacker_rank)
                
                hacker_rank += 1

                part_table = pd.DataFrame(list(zip(id_list, name_list, hacker_salt_rank_list,
                                            comment_list, comment_salt_score_list)),
                                    columns = ['id', 'hacker', 'hacker_salt_ranking',
                                            'comment', 'comment_saltiness_score'])
                                                #'hacker_specific_comment_rank'])
                
                full_table = pd.concat([full_table, part_table])
                
            return full_table

        ss = salt_scorer_mk2(df, ranker(salt_scorer_mk1(name_lister(df, 5), df)))
        print(ss.head())
        print('done')
        
        # print(ss.head())


        """
        Take stuff from dataframe and pupulate a model. 
        do i want to put this stuff in a model. if i do i need to gigure out 
        disconnect bewtween local and deployed server

        i feel like there is a way to send the data with jjson request
        by posting to api 

        that circumvents having a local model
        """

        response = requests.get(f'https://hackernewsapilambda.herokuapp.com/saltyuser/')
        print(response.text)
        url = 'https://hackernewsapilambda.herokuapp.com/saltyuser/'
        r = requests.post(url, json=ss.to_json(orient='records'))
        print(r.status_code)



        """
        send post with dataframe
        """
