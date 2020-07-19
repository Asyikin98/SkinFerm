import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO senexd (about, rate, top, comment, dari) VALUES (%s, %s, %s, %s, %s)"""


def crawl_url(pageUrl, exsend_arr):
    url = 'https://www.skinstore.com/b.-kamins-lactic-10/11286385.html'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    ex = soup.find_all('div', class_='primary-wrap column-row')

    try:
        for exd in ex :

            about = exd.find("div",{"class":"productDescription_synopsisContent"}).get_text().strip()
            rate = exd.find("span",{"class":"visually-hidden productReviews_aggregateRating_hiddenLabel"}).get_text().strip()
            top = exd.find("h2",{"class":"productReviews_topReviewsTitle"}).get_text().strip()
            comment = exd.find("p",{"class":"productReviews_topReviewsExcerpt"}).get_text().strip()
            dari = exd.find("div",{"class":"productReviews_footerDateAndName"}).get_text().strip()


            exsend_arr.append((about, rate, top, comment, dari))


    finally:
            return exsend_arr

exsend_arr = crawl_url("", [])
print(len(exsend_arr))
cursor.executemany(sql, exsend_arr)
conn.commit()
cursor.close()
conn.close()
