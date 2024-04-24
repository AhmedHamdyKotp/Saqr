import serpapi as se
import sys
from serpapi import GoogleSearch
import requests as re
import analyzer
def organizing(or_result):
    Data = []
    for item in or_result :
        url = item['link']
        title = item['title']
        snippet = item['snippet']
        data={"url":url,"title":title,"snippet":snippet}
        Data.append(data)
    analyzer.extract_profession(Data)
    



