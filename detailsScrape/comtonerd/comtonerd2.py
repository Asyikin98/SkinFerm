import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO comtonerd (about, rate, top, comment, dari) VALUES (%s, %s, %s, %s, %s)"""


def crawl_url(pageUrl, tonercomd_arr):
    url = 'https://www.skinstore.com/niod-ethylated-l-ascorbic-acid-30-network-30ml/11396691.html'
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


            tonercomd_arr.append((about, rate, top, comment, dari))


    finally:
            return tonercomd_arr

tonercomd_arr = crawl_url("", [])
print(len(tonercomd_arr))
cursor.executemany(sql, tonercomd_arr)
conn.commit()
cursor.close()
conn.close()
