from bs4 import BeautifulSoup
import requests
import json

cu = 'https://www.cuchd.in/'
cuContent = requests.get(cu)
soup = BeautifulSoup(cuContent.content, 'html.parser')
cuNavbar = soup.find(attrs={'id': 'navbarCollapse'})

options = cuNavbar.find_all('li')
data = dict()

for option in options:
    heading = option.find('a', href = True).text
    data[heading] = []

    for row in option.find_all('li'):
        data[heading].append((row.find('a', href = True)['href'], row.find('a', href = True).text))

links = {key: item for key, item in data.items() if item != []}
pages = dict()

for category, link in list(links.items()):
    pages[category] = dict()
    for l, title in link:
        linkContent = requests.get(cu + l)
        linkSoup = BeautifulSoup(linkContent.content, 'html.parser')
        #print(linkSoup.get_text().replace('\n', ' '))
        paragraphs = linkSoup.find_all('p')
        pages[category][title] = '\n'.join([para.get_text() for para in paragraphs])

with open('Data/info.json', 'w') as f:
    json.dump(pages, f, indent=2)