import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO normask (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, masknor_arr):
    url = 'https://www.skinstore.com/skin-care/skincare-concern/normal-combination.list?pageNumber=1&facetFilters=averageReviewScore_auto_content:%5B4+TO+5%5D|en_brand_content:Alchimie+Forever|en_brand_content:ESPA|en_brand_content:Jurlique|en_brand_content:Manuka+Doctor|en_brand_content:Murad|en_brand_content:Peter+Thomas+Roth|en_brand_content:REN+Clean+Skincare|en_skincareproducttype_content:Mask|en_brand_content:SkinCeuticals'
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


            masknor_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return masknor_arr

masknor_arr = crawl_url("", [])
print(len(masknor_arr))
cursor.executemany(sql, masknor_arr)
conn.commit()
cursor.close()
conn.close()
