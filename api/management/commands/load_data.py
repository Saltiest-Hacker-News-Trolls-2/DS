from django.core.management.base import BaseCommand, CommandError
from api.models import Items 
import requests as request
import random
import datetime
import html2text
import faster_than_requests as requests
import json


class Command(BaseCommand):
    help = 'Overwrites titles in database'

    # def add_arguments(self, parser):
    #     parser.add_argument('path', nargs=2, type=str)

    def handle(self, *args, **options):
        Items.objects.all().delete()
    
        print("loading data from Hacker News api... ")

        url = 'https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty'
        req = request.get(url).json()

        # removes html characters from data
        text_maker = html2text.HTML2Text()
        text_maker.ignore_links = True
        text_maker.bypass_tables = False
        text_maker.open_quote = True
        text_maker.close_quote = True
        count = 0
        for i in random.sample(range(0, req), 70000):
            response = requests.get2json(f'https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty')
            count+=1
            print(i, count)
            data = json.loads(response)

            if 'id' not in data:
                # raise ValueError("No target in given data")
                continue
            if 'by' not in data:
                # raise ValueError("No target in given data")
                continue
            if 'text' not in data:
                # raise ValueError("No target in given data")
                continue
            
            
        
            if data['type'] == 'comment':
                print('inserting into database')
                # print(data, '\n')
                
                text_conv = text_maker.handle(data['text'])
                '''
                Checking keys should be easier than this so maybe this can be a function. 
                '''
                Items.objects.create(
                    id = data['id'],
                    by = data['by'],
                    text = text_conv,
                )
            else:
                print('nope')


        
        