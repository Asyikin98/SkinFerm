import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO drymoist (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, moistdry_arr):
    url = 'https://www.ulta.com/skin-care-moisturizers?N=1z14102Znfo3xzZ2796Z1z13p3o'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
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


            moistdry_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return moistdry_arr

moistdry_arr = crawl_url("", [])
print(len(moistdry_arr))
cursor.executemany(sql, moistdry_arr)
conn.commit()
cursor.close()
conn.close()
