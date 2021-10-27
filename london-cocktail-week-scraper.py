# Import Statements
import requests
from bs4 import BeautifulSoup

# Get the Request from the URL
request = requests.get('https://londoncocktailweek.com/bars/search/?filter=0,0,0,0,12&search=')

# Parse the request
all_bars = BeautifulSoup(request.text, 'html.parser')
links = all_bars.select('.list__item')

bars = []
print(bars)