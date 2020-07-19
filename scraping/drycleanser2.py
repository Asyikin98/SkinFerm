import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO drycleanser (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, cleanserdry_arr):
    url = 'https://www.ulta.com/skin-care-cleansers-face-wash?N=vr4yvtZged12jZ12m55x1Z1b4ctgvZ27gsZ1z13p3o'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    cleanser = soup.find_all('div', class_='productQvContainer')

    try:
        for cleansers in cleanser :
            first_product_image = cleansers.find('img')['src']
            img_name = random.randrange(1,500)
            full_name = str(img_name) + ".jpg"
            urllib.request.urlretrieve(first_product_image, full_name)


            first_product_name = cleansers.find("h4",{"class":"prod-title"}).get_text().strip()
            first_product_price = cleansers.find("span",{"class":"regPrice"}).get_text().strip()
            first_product_rating = cleansers.find("label",{"class":"sr-only"}).get_text().strip()


            cleanserdry_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))


    finally:
            return cleanserdry_arr

cleanserdry_arr = crawl_url("", [])
print(len(cleanserdry_arr))
cursor.executemany(sql, cleanserdry_arr)
conn.commit()
cursor.close()
conn.close()
