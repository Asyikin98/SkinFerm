import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO comtoner (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, tonercom_arr):
    url = 'https://www.skinstore.com/skin-care/skincare-concern/normal-combination.list?pageNumber=1&facetFilters=averageReviewScore_auto_content:%5B4+TO+5%5D|en_brand_content:Erno+Laszlo|en_brand_content:Jurlique|en_brand_content:NEOSTRATA|en_brand_content:NIOD|en_brand_content:Skin+Authority|en_brand_content:SkinCeuticals|en_brand_content:StriVectin|en_skincareproducttype_content:Toner|en_brand_content:PCA+SKIN'
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

            first_product_name = toners.find('h3', class_='productBlock_productName').get_text().strip()
            first_product_price = toners.find('div', class_='productBlock_price').get_text().strip()
            first_product_rating = toners.find('span', class_='visually-hidden productBlock_rating_hiddenLabel').get_text().strip()


            tonercom_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return tonercom_arr

tonercom_arr = crawl_url("", [])
print(len(tonercom_arr))
cursor.executemany(sql, tonercom_arr)
conn.commit()
cursor.close()
conn.close()
