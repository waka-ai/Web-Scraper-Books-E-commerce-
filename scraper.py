# scraper.py - Scrape book prices from website
import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

books = []
for book in soup.find_all('article', class_='product_pod'):
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    books.append({'title': title, 'price': price})

# Save to CSV
with open('books.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'price'])
    writer.writeheader()
    writer.writerows(books)

print(f"Scraped {len(books)} books!")
