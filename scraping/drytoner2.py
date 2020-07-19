import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO drytoner (image, name, price, rating) VALUES (%s, %s, %s, %s)"""


def crawl_url(pageUrl, tonerdry_arr):
    url = 'https://www.ulta.com/skin-care-cleansers-toner?N=ov226nZ1z141cpZ1z141elZgc8oxvZ27gwZ1z13p3o'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    toner = soup.find_all('div', class_='productQvContainer')

    try:
        for toners in toner :
            first_product_image = toners.find('img')['src']
            img_name = random.randrange(1,500)
            full_name = str(img_name) + ".jpg"
            urllib.request.urlretrieve(first_product_image, full_name)

            first_product_name = toners.find("h4",{"class":"prod-title"}).get_text().strip()
            first_product_price = toners.find("span",{"class":"regPrice"}).get_text().strip()
            first_product_rating = toners.find("label",{"class":"sr-only"}).get_text().strip()


            tonerdry_arr.append((first_product_image, first_product_name, first_product_price, first_product_rating))

    finally:
            return tonerdry_arr

tonerdry_arr = crawl_url("", [])
print(len(tonerdry_arr))
cursor.executemany(sql, tonerdry_arr)
conn.commit()
cursor.close()
conn.close()
