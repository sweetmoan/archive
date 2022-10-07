from bs4 import BeautifulSoup
import requests,datetime
from colorama import Fore ,init, Style
import json
from facebook_scraper import get_posts, set_noscript
from facebook_scraper import get_group_info
init(autoreset=True)
colr_grn=Fore.GREEN

colr_yllow=Fore.YELLOW
def yts_hc():
    print(colr_yllow+'sequential yts scraping..')
    try:    
        source = requests.get('https://yts.mx/').text
    except:
        print('no internet..')
    
    soup = BeautifulSoup(source,'lxml')
    print(colr_grn+'popular downloads:')
    for a in soup.find_all('a', class_ = 'browse-movie-title',limit=4):
        print(a.text)
    print('')

def yts_ws():

    print('''
Marvel release date:
Thor: Love and Thunder	         July 8, 2022
Black Panther: Wakanda Forever	 November 11, 2022
The Guardians of the Galaxy      Holiday Special	Late / Holiday, 2022   
    ''')

    print(colr_yllow+'Searching -='=ff. keywords in yts..')
    fruits = "the princess","the good",'doctor','world','black'
    for x in fruits:
        print(colr_grn+f"'{x}'")
        for i in fruits:      
            source = requests.get(f'https://yts.mx/browse-movies/{x}/all/all/0/latest/0/all').text   
            soup = BeautifulSoup(source,'lxml')
        for a in soup.find_all('a', class_ = 'browse-movie-title'):
            print(a.text)
        print('')
        
def wmon():
    try:
        ginfo = get_group_info("VenomousAndOtherSnakesOfSiam")
        print(ginfo['id'])
    except:
        print('error')
        input()
wmon()


