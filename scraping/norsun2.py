import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO norsun (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, sunnor_arr):
    url = 'https://www.ulta.com/skin-care-suncare-sunscreen?N=27ffZ1z13p3l'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    sun = soup.find_all('div', class_='productQvContainer')

    try:
        for suns in sun :
            first_product_image = suns.find('img')['src']
            img_name = random.randrange(1,500)
            full_name = str(img_name) + ".jpg"
            urllib.request.urlretrieve(first_product_image, full_name)

            first_product_name = suns.find("h4",{"class":"prod-title"}).get_text().strip()
            first_product_price = suns.find("span",{"class":"regPrice"}).get_text().strip()
            first_product_rating = suns.find("label",{"class":"sr-only"}).get_text().strip()


            sunnor_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return sunnor_arr

sunnor_arr = crawl_url("", [])
print(len(sunnor_arr))
cursor.executemany(sql, sunnor_arr)
conn.commit()
cursor.close()
conn.close()
