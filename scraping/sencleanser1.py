import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO sencleanser (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, cleansersen_arr):
    url = 'https://www.skinstore.com/skin-care/cleansers.list?pageNumber=1&facetFilters=en_brand_content:Avene|en_brand_content:Bioderma|en_brand_content:DHC|averageReviewScore_auto_content:%5B4+TO+5%5D|en_skincareproducttype_content:Cleanser|en_skinconcern_content:Sensitive|en_brand_content:Balance+Me'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    cleanser = soup.find_all('li', class_='productListProducts_product')

    try:
        for cleansers in cleanser :
            first_product_image = cleansers.find('img')['src']
            img_name = random.randrange(1,500)
            full_name = str(img_name) + ".jpg"
            urllib.request.urlretrieve(first_product_image, full_name)

            first_product_name = cleansers.find("h3",{"class":"productBlock_productName"}).get_text().strip()
            first_product_price = cleansers.find("div",{"class":"productBlock_price"}).get_text().strip()
            first_product_rating = cleansers.find("span",{"class":"visually-hidden productBlock_rating_hiddenLabel"}).get_text().strip()


            cleansersen_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return cleansersen_arr

cleansersen_arr = crawl_url("", [])
print(len(cleansersen_arr))
cursor.executemany(sql, cleansersen_arr)
conn.commit()
cursor.close()
conn.close()
