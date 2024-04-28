import tkinter as tk
from tkinter import ttk
from serpapi import GoogleSearch
import sys
sys.path.append("src/modules")  
import scraper
import network_visualization as nv
import heatmap_visualization as hm
import Third_D_visualization as td

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

    tk.Button(results_window,text="Results",command=scraper.sres).pack(pady=(10,0))
    tk.Button(results_window, text="Networks", command=nv.make_the_nodes).pack(pady=(10,0))
    tk.Button(results_window, text="Heatmap",command= hm.start).pack(pady=(10,0))
    tk.Button(results_window, text="3D Modelling", command =td.action).pack(pady=(10,0))

    results_window.mainloop()

window = tk.Tk()
window.title("MainWindow")
window.geometry("640x480")
window.configure(bg = '#e3d9e7')
label = ttk.Label(window, text="Type Your serpAPI key here", font=("Bernard MT Condensed", 20))
label.place(x=160, y=50)

plainTextEdit = tk.Text(window, height=2, width=60)
plainTextEdit.place(x=60, y=90)

label_2 = ttk.Label(window, text="What are You looking for?", font=("Bernard MT Condensed", 20),)
label_2.place(x=160, y=160)

plainTextEdit_2 = tk.Text(window, height=2, width=60)
plainTextEdit_2.place(x=60, y=210)

label_3 = ttk.Label(window, text="Type your key words if needed\n\tSOON!", font=("Bernard MT Condensed", 20))
label_3.place(x=150, y=270)

# plainTextEdit_3 = tk.Text(window, height=2, width=60)
# plainTextEdit_3.place(x=60, y=330)

def on_search():
    api_key = plainTextEdit.get("1.0", "end-1c")
    search_term = plainTextEdit_2.get("1.0", "end-1c")
    result = search(api_key, search_term)
    label_3.config(text=result)

pushButton = ttk.Button(window, text="Search Now", command=on_search)
pushButton.place(x=270, y=410)

window.mainloop()
