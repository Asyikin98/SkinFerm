import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO sensun (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, sunsen_arr):
    url = 'https://www.ry.com.au/skin-care/sunscreen.list?pageNumber=1&facetFilters=en_skinconcern_content:Sensitive|averageReviewScore_auto_content:%5B4+TO+5%5D'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    sun = soup.find_all('li', class_='productListProducts_product')

    try:
        for suns in sun :
            first_product_image = suns.find('img')['src']
            img_name = random.randrange(1,500)
            full_name = str(img_name) + ".jpg"
            urllib.request.urlretrieve(first_product_image, full_name)

            first_product_name = suns.find("h3",{"class":"productBlock_productName"}).get_text().strip()
            first_product_price = suns.find("div",{"class":"productBlock_price"}).get_text().strip()
            first_product_rating = suns.find("span",{"class":"visually-hidden productBlock_rating_hiddenLabel"}).get_text().strip()


            sunsen_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return sunsen_arr

sunsen_arr = crawl_url("", [])
print(len(sunsen_arr))
cursor.executemany(sql, sunsen_arr)
conn.commit()
cursor.close()
conn.close()
