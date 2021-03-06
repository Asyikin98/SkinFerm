import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO drytoner (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, tonerdry_arr):
    url = 'https://www.skinstore.com/skin-care/skincare-concern/dry-skin.list?pageNumber=1&facetFilters=averageReviewScore_auto_content:%5B4+TO+5%5D|en_brand_content:Aesop|en_brand_content:Avene|en_brand_content:Dermalogica|en_brand_content:Elizabeth+Arden|en_brand_content:Juice+Beauty|en_brand_content:La+Roche-Posay|en_brand_content:PCA+SKIN|en_brand_content:SEKKISEI|en_skincareproducttype_content:Toner|en_brand_content:StriVectin'
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


            tonerdry_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return tonerdry_arr

tonerdry_arr = crawl_url("", [])
print(len(tonerdry_arr))
cursor.executemany(sql, tonerdry_arr)
conn.commit()
cursor.close()
conn.close()
