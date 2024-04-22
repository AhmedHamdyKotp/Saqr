
import serpapi as se
from serpapi import GoogleSearch
import requests as re
import os
from dotenv  import load_dotenv
import sys
env_API = 'data/.env'
load_dotenv(dotenv_path=env_API)
apik = os.getenv('S_API')
sys.path.append("src/modules")
import scraper 
    
def userInput(word):
    params = {
    "q": word, # the search term
    'engine': 'google',
    'hl':'en',
    'api_key': apik, 
    'num' : 100,
    }
    s = GoogleSearch(params)
    result = s.get_dict()  
    scraper.organizing(result['organic_results'])


if  __name__ == "__main__":
    print("Enter a word to look for:")
    wd = input()
    res = userInput(wd)
