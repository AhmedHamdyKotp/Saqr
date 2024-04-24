import serpapi as se
import requests as re
import sys
sys.path.append("src/modules")  
import scraper

def user_input(api_key: str) -> None:
    while True:
        print("Enter a word to look for (or 'exit' to quit):")
        search_term = input()
        print("Choose the Certen search engine you prefare : ")
        search_engines = ['google', 'bing', 'yahoo', 'duckduckgo', 'baidu', 'yandex', 'google_scholar']
        choice = input()
        if search_term.lower() == 'exit':
            break

        params = {
            "q": search_term,
            'engine': choice,
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
    user_input(api_key)
