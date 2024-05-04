import tkinter as tk
from tkinter import ttk
import webbrowser
import os
import requests
from bs4 import BeautifulSoup

DIRECTORY = 'data/processed/photos/'
txtDIRECTORY = 'data/processed/texts/'
linkDirec = 'data/processed/links/'
def scrap_it(url, window):
    """
    Scrape images from a given URL and save them to a directory.
    """
    def scrape_images():
        try:
            response = requests.get(url)
            response.raise_for_status()  
            soup = BeautifulSoup(response.content, 'html.parser')
            images = soup.select('div img')

            for i, img in enumerate(images, start=1):
                image_url = img['src']
                if image_url.startswith(('http://', 'https://')):  
                    image_response = requests.get(image_url)
                    image_response.raise_for_status()  
                    image_data = image_response.content

                    filename = f'img{i}.jpg'  
                    filepath = os.path.join(DIRECTORY, filename)
                    with open(filepath, 'wb') as file:
                        file.write(image_data)
                        print(f"Image {i} saved on photos file")

            print(f"Scraping images from {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error scraping images: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

# Add a function to scrape text and save it to a text file
    def scrape_text():
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = ' '.join([p.text for p in soup.find_all('p')])
            with open(txtDIRECTORY +'scraped_text.txt', 'w') as f:
                f.write(text)
            print(f"Text scraped and saved to scraped_text.txt")
        except requests.exceptions.RequestException as e:
            print(f"Error scraping text: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def scrape_links():
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a['href'] for a in soup.find_all('a', href=True)]
            with open(linkDirec +'scraped_links.txt', 'w') as f:
                for link in links:
                    f.write(link + '\n')
            print(f"Links scraped and saved to scraped_links.txt")
        except requests.exceptions.RequestException as e:
            print(f"Error scraping links: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    scrape_window = tk.Toplevel(window)
    scrape_window.geometry("300x200")
    scrape_window.configure(bg='#e3d9e7')  

    scrape_button_style = ttk.Style()
    scrape_button_style.configure('TButton', font=("Bernard MT Condensed", 12))

    ttk.Button(scrape_window, text="Scrape Images", command=scrape_images).pack(pady=(10,0))
    ttk.Button(scrape_window, text="Scrape Text", command=scrape_text).pack(pady=(10,0))
    ttk.Button(scrape_window, text="Scrape Links", command=scrape_links).pack(pady=(10,0))
    ttk.Button(scrape_window, text="Cancel", command=scrape_window.destroy).pack(pady=(10,0))
