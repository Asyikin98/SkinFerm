import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO oilymoist (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, moist_arr):
    url = 'https://www.ulta.com/skin-care-face-moisturizer?N=ged12jZ1b4ctgvZ1z13outZ1z141f9Z1kqweidZgc8oxvZ1z1410vZ27h9Z1z13p3j'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    moist = soup.find_all('div', class_='productQvContainer')

    try:
        for moists in moist :
            first_product_image = moists.find('img')['src']
            img_name = random.randrange(1,500)
            full_name = str(img_name) + ".jpg"
            urllib.request.urlretrieve(first_product_image, full_name)

            first_product_name = moists.find("h4",{"class":"prod-title"}).get_text().strip()
            first_product_price = moists.find("span",{"class":"regPrice"}).get_text().strip()
            first_product_rating = moists.find("label",{"class":"sr-only"}).get_text().strip()

            moist_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
        return moist_arr

moist_arr = crawl_url("", [])
print(len(moist_arr))
cursor.executemany(sql, moist_arr)
conn.commit()
cursor.close()
conn.close()
