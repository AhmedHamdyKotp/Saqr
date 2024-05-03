import tkinter as tk
from tkinter import ttk
import webbrowser

def scrap_it(url, window):
    def scrape_images():
        # Add your code to scrape images here
        print(f"Scraping images from {url}")

    def scrape_text():
        # Add your code to scrape text here
        print(f"Scraping text from {url}")

    def scrape_links():
        # Add your code to scrape links here
        print(f"Scraping links from {url}")

    scrape_window = tk.Toplevel(window)
    scrape_window.geometry("300x200")
    scrape_window.configure(bg='#e3d9e7')  

    scrape_button_style = ttk.Style()
    scrape_button_style.configure('TButton', font=("Bernard MT Condensed", 12))

    ttk.Button(scrape_window, text="Scrape Images", command=scrape_images).pack(pady=(10,0))
    ttk.Button(scrape_window, text="Scrape Text", command=scrape_text).pack(pady=(10,0))
    ttk.Button(scrape_window, text="Scrape Links", command=scrape_links).pack(pady=(10,0))
    ttk.Button(scrape_window, text="Cancel", command=scrape_window.destroy).pack(pady=(10,0))
