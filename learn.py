import requests
from bs4 import BeautifulSoup
urls='https://quotes.toscrape.com/'
reponse =requests.get(urls)
# print(reponse.content)
soup=BeautifulSoup(reponse.content,'html.parser')
quotes=soup.find_all('span',class_='text')
auther=soup.find_all('small',class_='author')

tags=soup.find_all('div',class_='tags')
for quote, author,tag in zip(quotes,auther,tags):
    print (f'Quotes:{quote.text}')
    print(f'auther:{author.text}')
    print('Tags:')
    for t in tag.find_all('a',class_='tag'):
        print(f'-{t.text}')
print()
