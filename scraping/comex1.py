import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO comex (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, excom_arr):
    url = 'https://www.skinstore.com/skin-care/skincare-concern/normal-combination.list?pageNumber=1&facetFilters=averageReviewScore_auto_content:%5B4+TO+5%5D|en_brand_content:Daily+Concepts|en_brand_content:Erno+Laszlo|en_brand_content:Kerstin+Florian|en_brand_content:NEOSTRATA|en_skincareproducttype_content:Exfoliator|en_brand_content:Paula%27s+Choice'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    ex = soup.find_all('li', class_='productListProducts_product')

    try:
        for exs in ex :
            first_product_image = exs.find('img')['src']
            img_name = random.randrange(1,500)
            full_name = str(img_name) + ".jpg"
            urllib.request.urlretrieve(first_product_image, full_name)

            first_product_name = exs.find('h3', class_='productBlock_productName').get_text().strip()
            first_product_price = exs.find('div', class_='productBlock_price').get_text().strip()
            first_product_rating = exs.find('span', class_='visually-hidden productBlock_rating_hiddenLabel').get_text().strip()


            excom_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return excom_arr

excom_arr = crawl_url("", [])
print(len(excom_arr))
cursor.executemany(sql, excom_arr)
conn.commit()
cursor.close()
conn.close()
