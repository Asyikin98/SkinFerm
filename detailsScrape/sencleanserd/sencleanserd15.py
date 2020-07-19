import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO sencleanserd (about, rate, top, comment, dari) VALUES (%s, %s, %s, %s, %s)"""


def crawl_url(pageUrl, cleansersend_arr):
    url = 'https://www.ulta.com/hi-bye-clean-up-mud-foam-cleanser?productId=pimprod2009074'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    cleanser = soup.find_all('div', class_='ProductDetail__productImage ProductDetail__productImage--withoutSwatches')

    try:
        for cleanserd in cleanser :
            about = soup.find("div",{"class":"ProductMainSection"}).get_text().strip()
            rate = soup.find("div",{"class":"ProductDetail__productContent"}).get_text().strip()
            top = soup.find("p",{"class":"MixedMenuButton__Text MixedMenuButton__Text--label"}).get_text().strip()
            comment = soup.find("div",{"class":"Collapsible__contentInner"}).get_text().strip()
            dari = soup.find("div",{"class":"ProductDetail__ingredients"}).get_text().strip()


            cleansersend_arr.append((about, rate, top, comment, dari))


    finally:
            return cleansersend_arr

cleansersend_arr = crawl_url("", [])
print(len(cleansersend_arr))
cursor.executemany(sql, cleansersend_arr)
conn.commit()
cursor.close()
conn.close()
