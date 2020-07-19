import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO noreye (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, eyenor_arr):
    url = 'https://www.ulta.com/skin-care-eye-treatments-eye-cream?N=1b4ctgvZ1z14100Zov226nZ1z13oycZg26igcZ1m2r75sZw3zm3yZp5kbbqZ27hkZ1z13p3l'
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


            eyenor_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return eyenor_arr

eyenor_arr = crawl_url("", [])
print(len(eyenor_arr))
cursor.executemany(sql, eyenor_arr)
conn.commit()
cursor.close()
conn.close()
