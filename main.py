import tkinter as tk
from tkinter import ttk
from serpapi import GoogleSearch
import sys
import json
sys.path.append("src/modules")  
import scraper
import network_visualization as nv
import heatmap_visualization as hm
import Third_D_visualization as td

api_key_entry = None
search_term_entry = None
feedback_label = None

def search(api_key, search_term):
    try:
        params = {
            "q": search_term,
            'engine': 'google',
            'hl': 'en',
            'api_key': api_key,
            'num': 100,
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        scraper.organizing(results['organic_results'])
        return "Search completed successfully!"
    except Exception as e:
        return f"An error occurred: {e}"
def searchk(api_key, search_term):
    try:
        params = {
            "q": search_term,
            'engine': 'google',
            'hl': 'en',
            'api_key': api_key,
            'num': 1000,
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        scraper.organizing_k(results['organic_results'])
        return "Search completed successfully!"
    except Exception as e:
        return f"An error occurred: {e}"
def show_results_window():
    results_window = tk.Toplevel()  
    results_window.title("Results")
    results_window.geometry("300x200")
    results_window.configure(bg='#e3d9e7')  

    results_button_style = ttk.Style()
    results_button_style.configure('TButton', font=("Bernard MT Condensed", 12))

    ttk.Button(results_window, text="Results", command=scraper.sres).pack(pady=(10,0))
    ttk.Button(results_window, text="Networks", command=nv.make_the_nodes).pack(pady=(10,0))
    ttk.Button(results_window, text="Heatmap", command=hm.start).pack(pady=(10,0))
    ttk.Button(results_window, text="3D Modelling", command=td.action).pack(pady=(10,0))
def show_results_window_k():
    results_window = tk.Toplevel()  
    results_window.title("Results")
    results_window.geometry("300x200")
    results_window.configure(bg='#e3d9e7')  

    results_button_style = ttk.Style()
    results_button_style.configure('TButton', font=("Bernard MT Condensed", 12))

    ttk.Button(results_window, text="Results", command=scraper.sres_k).pack(pady=(10,0))

def main():
    global api_key_entry, search_term_entry, feedback_label

    def on_search():
        api_key = api_key_entry.get("1.0", "end-1c")
        search_term = search_term_entry.get("1.0", "end-1c")
        
        if api_key and search_term:  
            if keywords_var.get():
                keywords = keywords_entry.get("1.0", "end-1c").split(" ")
                # Save the keywords to a JSON file
                with open('data/external/key_words.json', 'w') as f:
                    json.dump(keywords, f)
                result = searchk(api_key, search_term)
                feedback_label.config(text=result) 
            else :                 

                result = search(api_key, search_term)
                feedback_label.config(text=result)
                show_results_window()

            with open('data/processed/profession_found.json', 'w') as file:
                pass 
            with open('data/raw/xy_data.json', 'w') as file:
                pass 
            with open('data/rawgraph_dict.json', 'w') as file:
                pass 

        else:
            feedback_label.config(text="Please fill in all fields.")




    def toggle_keywords_entry():
        if keywords_var.get():
            feedback_label.place(x=150, y=280)
            keywords_entry.place(x=60, y=310)
        else:
            feedback_label.place_forget()
            keywords_entry.place_forget()
    root = tk.Tk()
    root.title("Saqr")
    root.configure(bg = '#e3d9e7')
    window_width = 640
    window_height = 480

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    label = ttk.Label(root, text="Type Your serpAPI key here", font=("Bernard MT Condensed", 20))
    label.place(x=160, y=50)

    api_key_entry = tk.Text(root, height=2, width=60)
    api_key_entry.place(x=60, y=90)

    label_2 = ttk.Label(root, text="What are You looking for?", font=("Bernard MT Condensed", 20),)
    label_2.place(x=160, y=160)

    search_term_entry = tk.Text(root, height=2, width=60)
    search_term_entry.place(x=60, y=210)
    keywords_var = tk.BooleanVar()

    keywords_checkbox = ttk.Checkbutton(root, text="Sign your own keywords", variable=keywords_var, command=toggle_keywords_entry)
    keywords_checkbox.place(relx=0.5, rely=0.55, anchor='center')

    feedback_label = ttk.Label(root, text="Type your key words if needed", font=("Bernard MT Condensed", 20))
    keywords_entry = tk.Text(root, height=2, width=60)

    pushButton = ttk.Button(root, text="Search Now", command=on_search)
    pushButton.place(x=270, y=410)

    root.mainloop()
if __name__ == "__main__":
    main()
