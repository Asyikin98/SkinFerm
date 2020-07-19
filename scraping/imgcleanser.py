import sys
import os
import csv
import pandas as pd
import urllib.request

def url_to_jpg(i, url, file_path):

    filename = 'image-{}.jpg'.format(i)
    full_path ='{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(url, full_path)

    print('{} saved.'.format(filename))

    return None

#constant
#FILENAME = 'cleanser.csv'
FILE_PATH = 'oilycleanserimg/'

#read url
df = pd.read_csv("Users/HP/Desktop/cleanser/c.csv")

#save img to
for i, url in enumerate(df.values):
    url_to_jpg(i, url[0], FILE_PATH)
