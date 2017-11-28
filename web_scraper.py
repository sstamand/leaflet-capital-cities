"""
Scraping Capital City Data
author: sstamand
created: November 26, 2017
"""

import requests
from bs4 import BeautifulSoup

url = "http://www.lab.lmnixon.org/4th/worldcapitals.html"
url_access = requests.get(url)
html_access = url_access.content

html = BeautifulSoup(html_access, 'lxml')

# 'tr' tag for each country
country_info = html.find_all('tr')

# create empty lists to store data
city_list = ["city"]
latitude_list = []
longitude_list = []

# populate lists by finding creating list item for all td tags under tr tag
for row in country_info[1:201]:
    cell = [i.text for i in row.find_all('td')]
    city_list.append(cell[1] + ", " + cell[0])
    latitude_list.append(cell[2])
    longitude_list.append(cell[3])

# create latitude list of float 
# and convert Southern hemisphere values to negative
lat = ["lat"]
for item in latitude_list:
    if item[5] == 'N':
        lat.append(float(item[0:5]))
    elif item[5] == 'S':
        lat.append(-float(item[0:5]))

# create longitude list of float 
# and convert Western hemisphere value to negative
lng = ["lng"]
for item in longitude_list:
    if item[5] == 'E':
        lng.append(float(item[0:5]))
    elif item[5] == 'W':
        lng.append(-float(item[0:5])) 
    elif item[6] == 'E':
        lng.append(float(item[0:6]))
    elif item[6] == 'W':
        lng.append(-float(item[0:6]))
        
## correct error in Jerusalem which should be 35E not W
lng.pop(city_list.index("Jerusalem, Israel"))
lng.insert(city_list.index("Jerusalem, Israel"),35.10)

data = zip(*[city_list, lat, lng])

with open('city_data.csv', 'w') as output:
    writer = csv.writer(output, lineterminator = '\n')
    writer.writerows(data)