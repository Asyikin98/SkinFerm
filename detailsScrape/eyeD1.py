import csv
from bs4 import BeautifulSoup
from requests import get

url = 'https://www.skinstore.com/perricone-md-face-finishing-firming-tinted-moisturizer-spf-30/11833558.html'
page = get(url)
soup = BeautifulSoup(page.text, 'html.parser')
type(soup)

#######################################################for product 1############################################################################

desc = soup.find('div', class_='productDescription_synopsisContent')
print(desc.get_text().strip())

rate = soup.find('span', class_='visually-hidden productReviews_aggregateRating_hiddenLabel')
print(rate.get_text().strip())

top = soup.find('h2', class_='productReviews_topReviewsTitle')
print(top.get_text().strip())

comment = soup.find('p', class_='productReviews_topReviewsExcerpt')
print(comment.get_text().strip())

by = soup.find('div', class_='productReviews_footerDateAndName')
print(by.get_text().strip())

with open('oilyeyeD1.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([desc.get_text().strip(), rate.get_text().strip(), top.get_text().strip(), comment.get_text().strip(), by.get_text().strip()])


csv_file.close()
