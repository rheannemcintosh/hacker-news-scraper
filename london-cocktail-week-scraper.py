# Import Statements
import requests
from bs4 import BeautifulSoup

# Get the Request from the URL
request = requests.get('https://londoncocktailweek.com/bars/print/?collectionId=0&whatId=0&areaId=0&spiritId=0&openNow=0&search=')

# Parse the request
all_bars = BeautifulSoup(request.text, 'html.parser')
bars = all_bars.select('.bar_name')

b = []
for i, item in enumerate(bars):
    title = item.getText()
    b.append(title)

print(b)