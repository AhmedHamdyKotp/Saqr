import sys
sys.path.append('src/utils')
sys.path.append('src/modules')

import scraper as sc
import constants 

def extract_profession(data):
    profession = constants.get_professions()    
    profession_found = {}

    for item in data:
        for i in profession:
            if i.lower() in item['title'].lower() or i.lower() in item['snippet'].lower():
                profession_found[i] = profession_found.get(i, []) + [item['url']]

    for profession, urls in profession_found.items():
        print(f"Profession: {profession}")
        for url in urls:
            print(f"URL: {url}")
        print("-------------------------")
    return profession_found


