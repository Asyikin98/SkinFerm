import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO drymask (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, maskdry_arr):
    url = 'https://www.ulta.com/skin-care-treatment-serums-face-masks?N=1z14102Z1z141cpZnfo3xzZ27hfZ1z13p3o'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
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


            maskdry_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))
 
    finally:
            return maskdry_arr

maskdry_arr = crawl_url("", [])
print(len(maskdry_arr))
cursor.executemany(sql, maskdry_arr)
conn.commit()
cursor.close()
conn.close()
