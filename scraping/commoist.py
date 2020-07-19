import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO commoist (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, moistcom_arr):
    url = 'https://www.ry.com.au/skin-care/normal-combination-skin.list?pageNumber=1&facetFilters=en_skincareproducttype_content:Moisturiser|averageReviewScore_auto_content:%5B4+TO+5%5D'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    moist = soup.find_all('li', class_='productListProducts_product')

    try:
        for moists in moist :
            first_product_image = moists.find('img')['src']
            img_name = random.randrange(1,500)
            full_name = str(img_name) + ".jpg"
            urllib.request.urlretrieve(first_product_image, full_name)

            first_product_name = moists.find('h3', class_='productBlock_productName').get_text().strip()
            first_product_price = moists.find('div', class_='productBlock_price').get_text().strip()
            first_product_rating = moists.find('span', class_='visually-hidden productBlock_rating_hiddenLabel').get_text().strip()


            moistcom_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return moistcom_arr

moistcom_arr = crawl_url("", [])
print(len(moistcom_arr))
cursor.executemany(sql, moistcom_arr)
conn.commit()
cursor.close()
conn.close()
