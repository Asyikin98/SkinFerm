import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO sencleanserd (about, rate, top, comment, dari) VALUES (%s, %s, %s, %s, %s)"""


def crawl_url(pageUrl, cleansersend_arr):
    url = 'https://www.skinstore.com/avene-extremely-gentle-cleanser-6.7fl.-oz/11117573.html'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    cleanser = soup.find_all('div', class_='primary-wrap column-row')

    try:
        for cleanserd in cleanser :

            about = cleanserd .find("div",{"class":"productDescription_synopsisContent"}).get_text().strip()
            rate = cleanserd .find("span",{"class":"visually-hidden productReviews_aggregateRating_hiddenLabel"}).get_text().strip()
            top = cleanserd .find("h2",{"class":"productReviews_topReviewsTitle"}).get_text().strip()
            comment = cleanserd .find("p",{"class":"productReviews_topReviewsExcerpt"}).get_text().strip()
            dari = cleanserd .find("div",{"class":"productReviews_footerDateAndName"}).get_text().strip()


            cleansersend_arr.append((about, rate, top, comment, dari))

    finally:
            return cleansersend_arr

cleansersend_arr = crawl_url("", [])
print(len(cleansersend_arr))
cursor.executemany(sql, cleansersend_arr)
conn.commit()
cursor.close()
conn.close()
