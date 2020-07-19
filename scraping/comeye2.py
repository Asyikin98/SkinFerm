import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO comeye (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, eyecom_arr):
    url = 'https://www.ulta.com/skin-care-eye-treatments-eye-cream?N=ged12jZov226nZ1z13oycZ1z1281xZ1z13oyzZw3zm3yZ1z13akaZgc8oxvZ27hkZ1z13p3k'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    eye = soup.find_all('div', class_='productQvContainer')

    try:
        for eyes in eye :
            first_product_image = eyes.find('img')['src']
            img_name = random.randrange(1,500)
            full_name = str(img_name) + ".jpg"
            urllib.request.urlretrieve(first_product_image, full_name)

            first_product_name = eyes.find("h4",{"class":"prod-title"}).get_text().strip()
            first_product_price = eyes.find("span",{"class":"regPrice"}).get_text().strip()
            first_product_rating = eyes.find("label",{"class":"sr-only"}).get_text().strip()


            eyecom_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return eyecom_arr

eyecom_arr = crawl_url("", [])
print(len(eyecom_arr))
cursor.executemany(sql, eyecom_arr)
conn.commit()
cursor.close()
conn.close()
