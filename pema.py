import requests
from bs4 import BeautifulSoup
urls='https://www.ktm.com/en-us/models/enduro.html#2stroke/'
reponse =requests.get(urls)
print(reponse.content)
soup=BeautifulSoup(reponse.content,'html.parser')
Components=soup.find_all('div',class_='wp-component')
Models=soup.find_all('span',class_='rte-font-ff6600')

heading=soup.find_all('h1',class_='CHALLENGE ACCEPTED! ')
for Components, Models,heading in zip(Components,Models,heading):
    print (f'Component:{Components.text}')
    print(f'Models:{Models.text}')
    print('heading:{heading.text}')
    for t in heading.find_all('a',class_='heading'):
        print(f'-{t.text}')
print()