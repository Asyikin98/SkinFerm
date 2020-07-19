import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO norsun (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, sunnor_arr):
    url = 'https://www.skinstore.com/skin-care/sunscreen.list?pageNumber=1&facetFilters=en_brand_content:DERMAdoctor|en_brand_content:Elemis|en_brand_content:Murad|en_brand_content:Obagi|en_brand_content:Paula%27s+Choice|en_brand_content:Perricone+MD|en_skinconcern_content:Normal|averageReviewScore_auto_content:%5B4+TO+5%5D|en_brand_content:Natura+Biss%C3%A9'
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


            sunnor_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return sunnor_arr

sunnor_arr = crawl_url("", [])
print(len(sunnor_arr))
cursor.executemany(sql, sunnor_arr)
conn.commit()
cursor.close()
conn.close()
