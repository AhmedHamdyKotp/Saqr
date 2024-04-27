import tkinter as tk
from serpapi import GoogleSearch
import sys
sys.path.append("src/modules")  
import scraper
import network_visualization as nv
import heatmap_visualization as hm
import Third_D_visualization as td

api_key_entry = None
search_term_entry = None
feedback_label = None
button_style = {'font': ('Helvetica', 12, 'bold'), 'bg': '#5499C7', 'fg': 'white', 'relief': 'groove', 'bd': 3}

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
def show_results_window():
    results_window = tk.Tk()
    results_window.title("Results")
    results_window.geometry("300x200")
    results_window.configure(bg="#D6EAF8")

    tk.Button(results_window,text="Results",command=scraper.sres,**button_style).pack(pady=(10,0))
    tk.Button(results_window, text="Networks", command=nv.make_the_nodes, **button_style).pack(pady=(10,0))
    tk.Button(results_window, text="Heatmap",command= hm.start,**button_style).pack(pady=(10,0))
    tk.Button(results_window, text="3D Modelling", command =td.action, **button_style).pack(pady=(10,0))

    results_window.mainloop()
def main():
    global api_key_entry, search_term_entry, feedback_label

    def on_search():
        feedback_label.config(text="Searching...")
        result = search(api_key_entry.get(), search_term_entry.get())
        feedback_label.config(text=result)
        show_results_window()

    def show_main_window():
        welcome_window.destroy()
        main_window()

    def main_window():
        global api_key_entry, search_term_entry, feedback_label

        root = tk.Tk()
        root.title("Saffa7 Trends")
        root.geometry("500x700")
        root.configure(bg="#D6EAF8")

        label_style = {'font': ('Helvetica', 12), 'bg': '#D6EAF8'}
        button_style = {'font': ('Helvetica', 12, 'bold'), 'bg': '#5499C7', 'fg': 'white', 'relief': 'groove', 'bd': 3}

        tk.Label(root, text="Enter your SerpAPI key:", **label_style).pack(pady=(10,0))
        api_key_entry = tk.Entry(root, font=('Helvetica', 10), bd=2)
        api_key_entry.pack(pady=(0,10))

        tk.Label(root, text="Enter a word to look for:", **label_style).pack(pady=(10,0))
        search_term_entry = tk.Entry(root, font=('Helvetica', 10), bd=2)
        search_term_entry.pack(pady=(0,10))

        tk.Button(root, text="Search", command=on_search, **button_style).pack(pady=(0,10))

        feedback_label = tk.Label(root, text="", **label_style)
        feedback_label.pack(pady=(10,0))

        root.mainloop()

    welcome_window = tk.Tk()
    welcome_window.title("Welcome")
    welcome_window.geometry("300x200")
    welcome_window.configure(bg="#D6EAF8")
    tk.Label(welcome_window, text="Welcome to Saffa7 Trends!", bg="#D6EAF8", font=("Helvetica", 16)).pack(expand=True)
    tk.Button(welcome_window, text="Continue", command=show_main_window, **button_style).pack(pady=(0,20))
    welcome_window.mainloop()

if __name__ == "__main__":
    main()
