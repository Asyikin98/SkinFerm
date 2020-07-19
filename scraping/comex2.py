import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO comex (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, excom_arr):
    url = 'https://www.ulta.com/skin-care-cleansers-exfoliators-scrubs?N=xabughZ1z141f9Z1g16u7lZ1z13oycZg26igcZ1z12qcmZqx96enZ27gvZ1z13p3k'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    ex = soup.find_all('div', class_='productQvContainer')

    try:
        for exs in ex :
            first_product_image = exs.find('img')['src']
            img_name = random.randrange(1,500)
            full_name = str(img_name) + ".jpg"
            urllib.request.urlretrieve(first_product_image, full_name)

            first_product_name = exs.find('h4', class_='prod-title').get_text().strip()
            first_product_price = exs.find('span', class_='regPrice').get_text().strip()
            first_product_rating = exs.find('label', class_='sr-only').get_text().strip()


            excom_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return excom_arr

excom_arr = crawl_url("", [])
print(len(excom_arr))
cursor.executemany(sql, excom_arr)
conn.commit()
cursor.close()
conn.close()
