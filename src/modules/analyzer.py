import sys
sys.path.append('src/utils')
sys.path.append('src/modules')
sys.path.append('tests/unit')
import network_visualization as v
import scraper as sc
import constants 
import mesh
import json

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
    with open('data/processed/profession_found.json', 'w') as f:
        json.dump(profession_found, f)

    print("Data saved to profession_found.json")
    # for profession, urls in profession_found.items():
    #     print(f"{choice}: {profession}")
    #     for url in urls:
    #         print(f"URL: {url}")
    #     print("-------------------------")
    #v.make_the_nodes(profession_found)
    # mesh.make_the_nodes(profession_found) # testing

