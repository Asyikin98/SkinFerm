import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO dryeye (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, eyedry_arr):
    url = 'https://www.ry.com.au/skin-care/dry-skin.list?pageNumber=1&facetFilters=en_skincareproducttype_content:Eye+Care|averageReviewScore_auto_content:%5B4+TO+5%5D'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    eye = soup.find_all('li', class_='productListProducts_product')

    try:
        for eyes in eye :
            first_product_image = eyes.find('img')['src']
            img_name = random.randrange(1,500)
            full_name = str(img_name) + ".jpg"
            urllib.request.urlretrieve(first_product_image, full_name)

            first_product_name = eyes.find("h3",{"class":"productBlock_productName"}).get_text().strip()
            first_product_price = eyes.find("div",{"class":"productBlock_price"}).get_text().strip()
            first_product_rating = eyes.find("span",{"class":"visually-hidden productBlock_rating_hiddenLabel"}).get_text().strip()


            eyedry_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return eyedry_arr

eyedry_arr = crawl_url("", [])
print(len(eyedry_arr))
cursor.executemany(sql, eyedry_arr)
conn.commit()
cursor.close()
conn.close()
