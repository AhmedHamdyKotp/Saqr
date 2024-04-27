import sys
import tkinter as tk
from tkinter import messagebox
sys.path.append('src/utils')
sys.path.append('src')
import main as mi
import constants 
import json
def extract_profession(data, choice):
    profession = constants.filter(choice)    
    profession_found = {}

    for item in data:
        for i in profession:
            if i.lower() in item['title'].lower() or i.lower() in item['snippet'].lower():
                profession_found[i] = profession_found.get(i, []) + [item['url']]
    with open('data/processed/profession_found.json', 'w') as f:
        json.dump(profession_found, f)
    mi.show_results_window()

def organizing(or_result):
    Data = []
    for item in or_result :
        url = item['link']
        title = item['title']
        snippet = item.get('snippet', "")
        data={"url":url,"title":title,"snippet":snippet if snippet else  ""}
        Data.append(data)
    main(Data)

def main(data):
    root = tk.Tk()
    root.title("Choose a Category")
    root.geometry("300x300")
    root.configure(bg="#D6EAF8")

    font_style = ('Helvetica', 14)

    label = tk.Label(root, text="Please select a category:", font=font_style, bg="#D6EAF8")
    label.pack(pady=(20,10))

    choices = ["Profession", "News", "Person", "General"]
    choice_var = tk.StringVar(root)
    choice_var.set(choices[0])

    drop_down_menu = tk.OptionMenu(root, choice_var, *choices)
    drop_down_menu.config(font=font_style)
    drop_down_menu.pack(pady=(0,20))

    submit_button = tk.Button(root, text="Submit", command=lambda: extract_profession(data, choice_var.get()), font=font_style, bg='#5499C7', fg='white')
    submit_button.pack(pady=(0,20))

    root.mainloop()


