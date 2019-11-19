from django.core.management.base import BaseCommand, CommandError
import pytz
from api.models import Items 
import requests
import random
import datetime
import html2text


class Command(BaseCommand):
    help = 'Overwrites titles in database'

    # def add_arguments(self, parser):
    #     parser.add_argument('path', nargs=2, type=str)

    def handle(self, *args, **options):
        Items.objects.all().delete()
    
        print("loading data from Hacker News api... ")

        url = 'https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty'
        req = requests.get(url).json()

        # removes html characters from data
        text_maker = html2text.HTML2Text()
        text_maker.ignore_links = True
        text_maker.bypass_tables = False
        text_maker.open_quote = True
        text_maker.close_quote = True

        for i in range(1, 46):
            response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty')
            if response.status_code == 200:            
                if response.json()['type'] == 'comment':
                    print(response.text)
                    print('ok')

                    text_conv = text_maker.handle(response.json()['text'])


                    '''
                    Checking keys should be easier than this so maybe this can be a function. 
                    '''
                    if 'text' and 'by' and 'id' not in response:
                        pass
                    
                    Items.objects.create(
                        id = response.json()['id'],
                        by = response.json()['by'],
                        text = text_conv,
                    )
                    
            else:
                print('nope', response.status_code)

        
        