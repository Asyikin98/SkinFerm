import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO drymoistd (about, rate, top, comment, dari) VALUES (%s, %s, %s, %s, %s)"""


def crawl_url(pageUrl, moistdryd_arr):
    url = 'https://www.skinstore.com/epionce-medical-barrier-cream-2.5oz/11287451.html'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    moist = soup.find_all('div', class_='primary-wrap column-row')

    try:
        for moistd in moist :

            about = moistd.find("div",{"class":"productDescription_synopsisContent"}).get_text().strip()
            rate = moistd.find("span",{"class":"visually-hidden productReviews_aggregateRating_hiddenLabel"}).get_text().strip()
            top = moistd.find("h2",{"class":"productReviews_topReviewsTitle"}).get_text().strip()
            comment = moistd.find("p",{"class":"productReviews_topReviewsExcerpt"}).get_text().strip()
            dari = moistd.find("div",{"class":"productReviews_footerDateAndName"}).get_text().strip()


            moistdryd_arr.append((about, rate, top, comment, dari))


    finally:
            return moistdryd_arr

moistdryd_arr = crawl_url("", [])
print(len(moistdryd_arr))
cursor.executemany(sql, moistdryd_arr)
conn.commit()
cursor.close()
conn.close()
