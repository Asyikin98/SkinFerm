import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO norsund (about, rate, top, comment, dari) VALUES (%s, %s, %s, %s, %s)"""


def crawl_url(pageUrl, sunnord_arr):
    url = 'https://www.skinstore.com/elemis-pro-collagen-marine-cream-spf-30-50ml/12328579.html'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    sun = soup.find_all('div', class_='primary-wrap column-row')

    try:
        for sund in sun :

            about = sund.find("div",{"class":"productDescription_synopsisContent"}).get_text().strip()
            rate = sund.find("span",{"class":"visually-hidden productReviews_aggregateRating_hiddenLabel"}).get_text().strip()
            top = sund.find("h2",{"class":"productReviews_topReviewsTitle"}).get_text().strip()
            comment = sund.find("p",{"class":"productReviews_topReviewsExcerpt"}).get_text().strip()
            dari = sund.find("div",{"class":"productReviews_footerDateAndName"}).get_text().strip()


            sunnord_arr.append((about, rate, top, comment, dari))


    finally:
            return sunnord_arr

sunnord_arr = crawl_url("", [])
print(len(sunnord_arr))
cursor.executemany(sql, sunnord_arr)
conn.commit()
cursor.close()
conn.close()
