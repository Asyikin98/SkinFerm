import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO drytonerd (about, rate, top, comment, dari) VALUES (%s, %s, %s, %s, %s)"""


def crawl_url(pageUrl, tonerdryd_arr):
    url = 'https://www.skinstore.com/aesop-parsley-seed-anti-oxidant-toner-200ml/11536610.html'
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


            tonerdryd_arr.append((about, rate, top, comment, dari))


    finally:
            return tonerdryd_arr

tonerdryd_arr = crawl_url("", [])
print(len(tonerdryd_arr))
cursor.executemany(sql, tonerdryd_arr)
conn.commit()
cursor.close()
conn.close()
