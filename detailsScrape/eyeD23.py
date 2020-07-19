import csv
from bs4 import BeautifulSoup
from requests import get

url = 'https://www.ulta.com/superdefense-spf-25-fatigue-1st-signs-of-age-muti-correcting-cream-combination-oily-oily-skin?productId=pimprod2014016'
page = get(url)
soup = BeautifulSoup(page.text, 'html.parser')
type(soup)

#######################################################for product 1############################################################################
pro = soup.find('div', class_='ProductMainSection')
print(pro.get_text().strip())

desc = soup.find('div', class_='ProductDetail__productContent')
print(desc.get_text().strip())

use = soup.find('p', class_='MixedMenuButton__Text MixedMenuButton__Text--label')
print(use.get_text().strip())

huse = soup.find('div', class_='ProductDetail__productContent')
print(huse.get_text().strip())

ing = soup.find('div', class_='ProductDetail__ingredients')
print(ing.get_text().strip())


with open('oilyeyeD.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([pro.get_text().strip(), desc.get_text().strip(), use.get_text().strip(), huse.get_text().strip(), ing.get_text().strip()])


csv_file.close()
