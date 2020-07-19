import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO comcleanser (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, cleansercom_arr):
    url = 'https://www.skinstore.com/skin-care/cleansers.list?pageNumber=1&facetFilters=en_brand_content:Balance+Me|en_brand_content:Caudalie|en_brand_content:Daily+Concepts|en_brand_content:Epionce|en_brand_content:Erno+Laszlo|en_brand_content:First+Aid+Beauty|en_brand_content:Gallin%C3%A9e|en_brand_content:High+Beauty|en_brand_content:skyn+ICELAND|en_brand_content:Vichy|averageReviewScore_auto_content:%5B4+TO+5%5D|en_skincareproducttype_content:Cleanser|en_skinconcern_content:Combination+Skin|en_brand_content:Kerstin+Florian'
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

            first_product_name = cleansers.find('h3', class_='productBlock_productName').get_text().strip()
            first_product_price = cleansers.find('div', class_='productBlock_price').get_text().strip()
            first_product_rating = cleansers.find('span', class_='visually-hidden productBlock_rating_hiddenLabel').get_text().strip()


            cleansercom_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return cleansercom_arr

cleansercom_arr = crawl_url("", [])
print(len(cleansercom_arr))
cursor.executemany(sql, cleansercom_arr)
conn.commit()
cursor.close()
conn.close()
