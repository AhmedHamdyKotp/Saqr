import sys
import tkinter as tk
from tkinter import messagebox
sys.path.append('src/utils')
sys.path.append('src')
import main as mi
import constants 
import json
from tkinter import font as tkfont
import webbrowser
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

def callback(url):
    webbrowser.open_new(url)


def sres():
    with open('data/processed/profession_found.json', 'r') as f:
        profession_found = json.load(f)  
    window = tk.Tk()
    window.title("Profession Data")
    window.geometry("500x500")
    window.configure(bg='#e3d9e7') 

    font_style = tkfont.Font(family="Bernard MT Condensed", size=14)

    scrollbar = tk.Scrollbar(window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text = tk.Text(window, yscrollcommand=scrollbar.set, font=font_style, bg='#e3d9e7', wrap=tk.WORD)  # Same background color
    text.pack(side=tk.LEFT, fill=tk.BOTH)
    for profession, urls in profession_found.items():
        text.insert(tk.END, f"Category: {profession}\n")
        for url in urls:
            text.insert(tk.END, "URL: ")
            text.insert(tk.END, f"{url}\n", (url,))
            text.tag_config(url, foreground="blue", underline=1)
            text.tag_bind(url, "<Button-1>", lambda e, url=url: callback(url))

    scrollbar.config(command=text.yview)

    window.mainloop()


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
    root.configure(bg='#e3d9e7') 

    font_style = ('Bernard MT Condensed', 14)  

    label = tk.Label(root, text="Please select a category:", font=font_style, bg='#e3d9e7')  
    label.pack(pady=(20,10))

    choices = ["Profession", "News", "Person", "General"]
    choice_var = tk.StringVar(root)
    choice_var.set(choices[0])

    drop_down_menu = tk.OptionMenu(root, choice_var, *choices)
    drop_down_menu.config(font=font_style, bg='#e3d9e7') 
    drop_down_menu.pack(pady=(0,20))

    submit_button = tk.Button(root, text="Submit", command=lambda: extract_profession(data, choice_var.get()), font=font_style, bg='#5499C7', fg='white')
    submit_button.pack(pady=(0,20))

    root.mainloop()


