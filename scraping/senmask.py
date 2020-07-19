import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO senmask (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, masksen_arr):
    url = 'https://www.ry.com.au/skin-care/sensitive-skin.list?pageNumber=1&facetFilters=averageReviewScore_auto_content:%5B4+TO+5%5D|en_skincareproducttype_content:Mask'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    mask = soup.find_all('li', class_='productListProducts_product')

    try:
        for masks in mask :
            first_product_image = masks.find('img')['src']
            img_name = random.randrange(1,500)
            full_name = str(img_name) + ".jpg"
            urllib.request.urlretrieve(first_product_image, full_name)

            first_product_name = masks.find("h3",{"class":"productBlock_productName"}).get_text().strip()
            first_product_price = masks.find("div",{"class":"productBlock_price"}).get_text().strip()
            first_product_rating = masks.find("span",{"class":"visually-hidden productBlock_rating_hiddenLabel"}).get_text().strip()


            masksen_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return masksen_arr

masksen_arr = crawl_url("", [])
print(len(masksen_arr))
cursor.executemany(sql, masksen_arr)
conn.commit()
cursor.close()
conn.close()
