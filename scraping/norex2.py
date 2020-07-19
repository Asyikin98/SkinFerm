import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO norex (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, exnor_arr):
    url = 'https://www.ulta.com/skin-care-cleansers-exfoliators-scrubs?N=ged12jZ1z141f9Zirpok5Z1z1411bZ93pel9Z1z12qcjZqx96enZ1z1410vZ27gvZ1z13p3l'
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

            first_product_name = exs.find("h4",{"class":"prod-title"}).get_text().strip()
            first_product_price = exs.find("span",{"class":"regPrice"}).get_text().strip()
            first_product_rating = exs.find("label",{"class":"sr-only"}).get_text().strip()


            exnor_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return exnor_arr

exnor_arr = crawl_url("", [])
print(len(exnor_arr))
cursor.executemany(sql, exnor_arr)
conn.commit()
cursor.close()
conn.close()
