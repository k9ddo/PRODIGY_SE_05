import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import csv

def scrape_books():
    try:
        url = url_entry.get()
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        with open('books.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Price', 'Rating'])
            for book in books:
                title = book.h3.a['title']
                price = book.find('p', class_='price_color').text
                rating = book.p['class'][1]
                writer.writerow([title, price, rating])

        messagebox.showinfo("Success", "Scraped data saved to books.csv")
    except Exception as e:
        messagebox.showerror("Error", str(e))

scraper = tk.Tk()
scraper.title("Book Scraper")
scraper.geometry("400x150")

tk.Label(scraper, text="Enter URL to scrape:").pack(pady=5)
url_entry = tk.Entry(scraper, width=50)
url_entry.insert(0, "https://books.toscrape.com/")
url_entry.pack()

tk.Button(scraper, text="Scrape Books", command=scrape_books).pack(pady=10)

scraper.mainloop()
