import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')

def create_custom_hn(links, votes):
    hn = []

    for i, item in enumerate(links):
        title = links[i].getText()
        href = links[i].get('href', None)
        vote = int(votes[i].getText().replace(' points', ''))
        hn.append({'title': title, 'link': href})
        

    return hn

print(create_custom_hn(links, votes))