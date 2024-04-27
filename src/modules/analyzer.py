# import sys
# sys.path.append('src/modules')
# sys.path.append('tests/unit')
# import network_visualization as v
# import scraper as sc
# import mesh
# import json

# import tkinter as tk
# from tkinter import messagebox

# def extract_profession(data, choice):
#     profession = constants.filter(choice)    
#     profession_found = {}

#     for item in data:
#         for i in profession:
#             if i.lower() in item['title'].lower() or i.lower() in item['snippet'].lower():
#                 profession_found[i] = profession_found.get(i, []) + [item['url']]
#     with open('data/processed/profession_found.json', 'w') as f:
#         json.dump(profession_found, f)

#     messagebox.showinfo("Information", "Data saved to profession_found.json")

# def main():
#     root = tk.Tk()
#     root.title("Choose a Category")
#     root.geometry("500x00")

#     choices = ["Professions", "News", "Person", "General"]
#     choice_var = tk.StringVar(root)
#     choice_var.set(choices[0])

#     drop_down_menu = tk.OptionMenu(root, choice_var, *choices)
#     drop_down_menu.pack()

#     submit_button = tk.Button(root, text="Submit", command=lambda: extract_profession(data, choice_var.get()))
#     submit_button.pack()

#     root.mainloop()

# if __name__ == "__main__":
#     main()

#     # for profession, urls in profession_found.items():
#     #     print(f"{choice}: {profession}")
#     #     for url in urls:
#     #         print(f"URL: {url}")
#     #     print("-------------------------")
#     #v.make_the_nodes(profession_found)
#     # mesh.make_the_nodes(profession_found) # testing

