import urllib.request
import random
from bs4 import BeautifulSoup
from requests import get
import mysql.connector

conn = mysql.connector.connect(user="root", passwd="",host="localhost", database="product")

cursor = conn.cursor()

sql = """INSERT INTO normaskd (about, rate, top, comment, dari) VALUES (%s, %s, %s, %s, %s)"""


def crawl_url(pageUrl, masknord_arr):
    url = 'https://www.skinstore.com/murad-clarifying-mask/11292033.html'
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    #######################################################for product 1############################################################################
    mask = soup.find_all('div', class_='primary-wrap column-row')

    try:
        for maskd in mask :

            about = maskd.find("div",{"class":"productDescription_synopsisContent"}).get_text().strip()
            rate = maskd.find("span",{"class":"visually-hidden productReviews_aggregateRating_hiddenLabel"}).get_text().strip()
            top = maskd.find("h2",{"class":"productReviews_topReviewsTitle"}).get_text().strip()
            comment = maskd.find("p",{"class":"productReviews_topReviewsExcerpt"}).get_text().strip()
            dari = maskd.find("div",{"class":"productReviews_footerDateAndName"}).get_text().strip()


            masknord_arr.append((about, rate, top, comment, dari))


    finally:
            return masknord_arr

masknord_arr = crawl_url("", [])
print(len(masknord_arr))
cursor.executemany(sql, masknord_arr)
conn.commit()
cursor.close()
conn.close()
