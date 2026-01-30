"""
Web Scraping Mini Project
Scrapes all 4 and 5 star rated books from books.toscrape.com
Author: David Guerrero
"""


import requests
import bs4

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

print(f"{"Book Title".ljust(120)}Rating\t\tPage Number")
print("-"*160)

for i in range(1, 51):
    url = base_url.format(i)
    pagina = requests.get(url)
    sopa = bs4.BeautifulSoup(pagina.text, "lxml")
    libros = sopa.select(".product_pod")

    for libro in libros:
        if libro.select(".star-rating.Four") or libro.select(".star-rating.Five"):
            titulo = libro.select("h3 a")[0]["title"]
            rating = libro.select("p.star-rating")[0]["class"][1]
            
            print(f"{titulo.ljust(120)}{rating}\t\t{i}")

 
