import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO oilymask (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, mask_arr):
    url = 'https://www.ulta.com/skin-care-treatment-serums-face-masks?N=1z14102Z72casaZov226nZ1z141cpZ1ef51j6Z1z123ahZ1z1410vZ27hfZ1z13p3j'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    mask = soup.find_all('div', class_='productQvContainer')

    try:
        for masks in mask :
            first_product_image = masks.find('img')['src']
            img_name = random.randrange(1,500)
            full_name = str(img_name) + ".jpg"
            urllib.request.urlretrieve(first_product_image, full_name)

            first_product_name = masks.find("h4",{"class":"prod-title"}).get_text().strip()
            first_product_price = masks.find("span",{"class":"regPrice"}).get_text().strip()
            first_product_rating = masks.find("label",{"class":"sr-only"}).get_text().strip()

            mask_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
        return mask_arr

mask_arr = crawl_url("", [])
print(len(mask_arr))
cursor.executemany(sql, mask_arr)
conn.commit()
cursor.close()
conn.close()
