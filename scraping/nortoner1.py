import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO nortoner (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, tonernor_arr):
    url = 'https://www.skinstore.com/skin-care/skincare-concern/normal-combination.list?pageNumber=1&facetFilters=averageReviewScore_auto_content:%5B4+TO+5%5D|en_brand_content:Caudalie|en_brand_content:Erno+Laszlo|en_brand_content:Skin+Authority|en_skincareproducttype_content:Toner|en_brand_content:NEOSTRATA'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    toner = soup.find_all('li', class_='productListProducts_product')

    try:
        for toners in toner :
            first_product_image = toners.find('img')['src']
            img_name = random.randrange(1,500)
            full_name = str(img_name) + ".jpg"
            urllib.request.urlretrieve(first_product_image, full_name)

            first_product_name = toners.find("h3",{"class":"productBlock_productName"}).get_text().strip()
            first_product_price = toners.find("div",{"class":"productBlock_price"}).get_text().strip()
            first_product_rating = toners.find("span",{"class":"visually-hidden productBlock_rating_hiddenLabel"}).get_text().strip()


            tonernor_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return tonernor_arr

tonernor_arr = crawl_url("", [])
print(len(tonernor_arr))
cursor.executemany(sql, tonernor_arr)
conn.commit()
cursor.close()
conn.close()
