import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO drytonerd (about, rate, top, comment, dari) VALUES (%s, %s, %s, %s, %s)"""


def crawl_url(pageUrl, tonerdryd_arr):
    url = 'https://www.ulta.com/clarifying-lotion-1-very-dry-dry-skin?productId=xlsImpprod10791735'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    toner = soup.find_all('div', class_='ProductDetail__productImage ProductDetail__productImage--withoutSwatches')

    try:
        for tonerd in toner :
            about = soup.find("div",{"class":"ProductMainSection"}).get_text().strip()
            rate = soup.find("div",{"class":"ProductDetail__productContent"}).get_text().strip()
            top = soup.find("p",{"class":"MixedMenuButton__Text MixedMenuButton__Text--label"}).get_text().strip()
            comment = soup.find("div",{"class":"Collapsible__contentInner"}).get_text().strip()
            dari = soup.find("div",{"class":"ProductDetail__ingredients"}).get_text().strip()


            tonerdryd_arr.append((about, rate, top, comment, dari))


    finally:
            return tonerdryd_arr

tonerdryd_arr = crawl_url("", [])
print(len(tonerdryd_arr))
cursor.executemany(sql, tonerdryd_arr)
conn.commit()
cursor.close()
conn.close()
