#learning
import requests
from bs4 import BeautifulSoup
url='https://hdkharak.org/'
response=requests.get(url)
soup=BeautifulSoup(response.content,'html.parser')
content=soup.find_all('div',id_='content')


titles = soup.find_all('h2', class_='elementor-heading-title')
for title in titles:
    print(title.text)
    