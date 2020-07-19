import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO oilytonerd (about, rate, top, comment, dari) VALUES (%s, %s, %s, %s, %s)"""


def crawl_url(pageUrl, toneroilyd_arr):
    url = 'https://www.skinstore.com/caudalie-instant-foaming-cleanser-150ml/10727688.html'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    toner = soup.find_all('div', class_='primary-wrap column-row')

    try:
        for tonerd in toner :

            about = tonerd.find("div",{"class":"productDescription_synopsisContent"}).get_text().strip()
            rate = tonerd.find("span",{"class":"visually-hidden productReviews_aggregateRating_hiddenLabel"}).get_text().strip()
            top = tonerd.find("h2",{"class":"productReviews_topReviewsTitle"}).get_text().strip()
            comment = tonerd.find("p",{"class":"productReviews_topReviewsExcerpt"}).get_text().strip()
            dari = tonerd.find("div",{"class":"productReviews_footerDateAndName"}).get_text().strip()


            toneroilyd_arr.append((about, rate, top, comment, dari))


    finally:
            return toneroilyd_arr

toneroilyd_arr = crawl_url("", [])
print(len(toneroilyd_arr))
cursor.executemany(sql, toneroilyd_arr)
conn.commit()
cursor.close()
conn.close()
