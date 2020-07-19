import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO seneyed (about, rate, top, comment, dari) VALUES (%s, %s, %s, %s, %s)"""


def crawl_url(pageUrl, eyesend_arr):
    url = 'https://www.skinstore.com/perricone-md-essential-fx-acyl-glutathione-eyelid-lift-serum/11833577.html'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    eye = soup.find_all('div', class_='primary-wrap column-row')

    try:
        for eyed in eye :

            about = eyed.find("div",{"class":"productDescription_synopsisContent"}).get_text().strip()
            rate = eyed.find("span",{"class":"visually-hidden productReviews_aggregateRating_hiddenLabel"}).get_text().strip()
            top = eyed.find("h2",{"class":"productReviews_topReviewsTitle"}).get_text().strip()
            comment = eyed.find("p",{"class":"productReviews_topReviewsExcerpt"}).get_text().strip()
            dari = eyed.find("div",{"class":"productReviews_footerDateAndName"}).get_text().strip()


            eyesend_arr.append((about, rate, top, comment, dari))


    finally:
            return eyesend_arr

eyesend_arr = crawl_url("", [])
print(len(eyesend_arr))
cursor.executemany(sql, eyesend_arr)
conn.commit()
cursor.close()
conn.close()
