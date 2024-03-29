import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO drycleanserd (about, rate, top, comment, dari) VALUES (%s, %s, %s, %s, %s)"""


def crawl_url(pageUrl, cleanserdryd_arr):
    url = 'https://www.ulta.com/seriously-soothing-cleansing-cream?productId=pimprod2006230'
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


            cleanserdryd_arr.append((about, rate, top, comment, dari))


    finally:
            return cleanserdryd_arr

cleanserdryd_arr = crawl_url("", [])
print(len(cleanserdryd_arr))
cursor.executemany(sql, cleanserdryd_arr)
conn.commit()
cursor.close()
conn.close()
