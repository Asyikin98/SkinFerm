import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO normoist (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, moistnor_arr):
    url = 'https://www.ulta.com/24-7-moisture-hydrating-day-night-cream?productId=xlsImpprod18731039'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    moist = soup.find_all('div', class_='productQvContainer')

    try:
        for moists in moist :
            first_product_image = moists.find('img')['src']
            img_name = random.randrange(1,500)
            full_name = str(img_name) + ".jpg"
            urllib.request.urlretrieve(first_product_image, full_name)

            first_product_name = moists.find("h4",{"class":"prod-title"}).get_text().strip()
            first_product_price = moists.find("span",{"class":"regPrice"}).get_text().strip()
            first_product_rating = moists.find("label",{"class":"sr-only"}).get_text().strip()


            moistnor_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return moistnor_arr

moistnor_arr = crawl_url("", [])
print(len(moistnor_arr))
cursor.executemany(sql, moistnor_arr)
conn.commit()
cursor.close()
conn.close()
