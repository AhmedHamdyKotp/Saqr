import tkinter as tk
from tkinter import ttk
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
    results_window = tk.Toplevel()  # Use Toplevel() instead of Tk()
    results_window.title("Results")
    results_window.geometry("300x200")
    results_window.configure(bg="#D6EAF8")

    tk.Button(results_window,text="Results",command=scraper.sres).pack(pady=(10,0))
    tk.Button(results_window, text="Networks", command=nv.make_the_nodes).pack(pady=(10,0))
    tk.Button(results_window, text="Heatmap",command= hm.start).pack(pady=(10,0))
    tk.Button(results_window, text="3D Modelling", command =td.action).pack(pady=(10,0))

def main():
    global api_key_entry, search_term_entry, feedback_label

    def on_search():
        api_key = api_key_entry.get("1.0", "end-1c")
        search_term = search_term_entry.get("1.0", "end-1c")
        if api_key and search_term:  # checks if both fields are not empty
            result = search(api_key, search_term)
            feedback_label.config(text=result)
            show_results_window()
        else:
            feedback_label.config(text="Please fill in all fields.")

    root = tk.Tk()
    root.title("MainWindow")
    root.geometry("640x480")
    root.configure(bg = '#e3d9e7')

    label = ttk.Label(root, text="Type Your serpAPI key here", font=("Bernard MT Condensed", 20))
    label.place(x=160, y=50)

    api_key_entry = tk.Text(root, height=2, width=60)
    api_key_entry.place(x=60, y=90)

    label_2 = ttk.Label(root, text="What are You looking for?", font=("Bernard MT Condensed", 20),)
    label_2.place(x=160, y=160)

    search_term_entry = tk.Text(root, height=2, width=60)
    search_term_entry.place(x=60, y=210)

    feedback_label = ttk.Label(root, text="Type your key words if needed\n\tSOON!", font=("Bernard MT Condensed", 20))
    feedback_label.place(x=150, y=270)

    pushButton = ttk.Button(root, text="Search Now", command=on_search)
    pushButton.place(x=270, y=410)

    root.mainloop()

if __name__ == "__main__":
    main()
