import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO normoistd (about, rate, top, comment, dari) VALUES (%s, %s, %s, %s, %s)"""


def crawl_url(pageUrl, moistnord_arr):
    url = 'https://www.ulta.com/travel-size-sweet-hydration-moisturizer?productId=pimprod2009713'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    moist = soup.find_all('div', class_='ProductDetail__productImage ProductDetail__productImage--withoutSwatches')

    try:
        for moistd in moist :
            about = soup.find("div",{"class":"ProductMainSection"}).get_text().strip()
            rate = soup.find("div",{"class":"ProductDetail__productContent"}).get_text().strip()
            top = soup.find("p",{"class":"MixedMenuButton__Text MixedMenuButton__Text--label"}).get_text().strip()
            comment = soup.find("div",{"class":"Collapsible__contentInner"}).get_text().strip()
            dari = soup.find("div",{"class":"ProductDetail__ingredients"}).get_text().strip()


            moistnord_arr.append((about, rate, top, comment, dari))


    finally:
            return moistnord_arr

moistnord_arr = crawl_url("", [])
print(len(moistnord_arr))
cursor.executemany(sql, moistnord_arr)
conn.commit()
cursor.close()
conn.close()
