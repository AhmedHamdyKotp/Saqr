import serpapi as se
import requests as re
import sys
sys.path.append("src/modules")  
import scraper

def user_input(api_key: str, search_term: str) -> None:

    params = {
        "q": search_term,
        'engine': 'google',
        'hl':'en',
        'api_key': api_key,
        'num' : 100,
    }

    search = se.GoogleSearch(params)
    result = search.get_dict()
    scraper.organizing(result['organic_results'])

if __name__ == "__main__":
    print("Enter your SerpAPI key: ")
    api_key = input()
    print("Enter a word to look for:")
    search_term = input()
    user_input(api_key, search_term)
