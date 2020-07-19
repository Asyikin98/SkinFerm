import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO drymask (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, maskdry_arr):
    url = 'https://www.skinstore.com/skin-care/skincare-concern/dry-skin.list?pageNumber=1&facetFilters=averageReviewScore_auto_content:%5B4+TO+5%5D|en_brand_content:Dr+Dennis+Gross+Skincare|en_brand_content:Elemis|en_brand_content:ESPA|en_brand_content:Jurlique|en_brand_content:Kerstin+Florian|en_brand_content:Murad|en_brand_content:Peter+Thomas+Roth|en_brand_content:SkinCeuticals|en_brand_content:SkinStore|en_brand_content:skyn+ICELAND|en_brand_content:TONYMOLY|en_brand_content:Vichy|en_skincareproducttype_content:Mask|en_brand_content:this+works'
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


            maskdry_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return maskdry_arr

maskdry_arr = crawl_url("", [])
print(len(maskdry_arr))
cursor.executemany(sql, maskdry_arr)
conn.commit()
cursor.close()
conn.close()
