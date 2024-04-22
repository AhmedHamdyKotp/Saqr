
import serpapi as se
from serpapi import GoogleSearch
import requests as re
import os
from dotenv  import load_dotenv
env_API = 'data/.env'
load_dotenv(dotenv_path=env_API)
apik = os.getenv('S_API')

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
    organizing(result['organic_results'])
    return result

def organizing(or_result):
    Data = []
    for item in or_result :
        url = item['link']
        title = item['title']
        snippet = item['snippet']
        data={"url":url,"title":title,"snippet":snippet}
        Data.append(data)
    for i in Data :
        print(i)
        print("-------------------------") 
    
    

userInput("Zewail City")
organizing()
