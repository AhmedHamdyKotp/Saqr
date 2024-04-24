import sys
sys.path.append('src/utils')
sys.path.append('src/modules')
import visualizer as v
import scraper as sc
import constants 

def extract_profession(data):
    print("Choose from these categories : ")
    print("ProfessionS\nNews\nPerson\nGeneral")
    choice = input()
    profession = constants.filter(choice)    
    profession_found = {}

    for item in data:
        for i in profession:
            if i.lower() in item['title'].lower() or i.lower() in item['snippet'].lower():
                profession_found[i] = profession_found.get(i, []) + [item['url']]

    for profession, urls in profession_found.items():
        print(f"{choice}: {profession}")
        for url in urls:
            print(f"URL: {url}")
        print("-------------------------")
    v.make_the_nodes(profession_found)
    return profession_found


