# Import Statements
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import requests


# Get relevant stories from hacker news
def create_custom_hn(links, subtext):
    for i, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[i].select('.score')

        if len(vote):
            votes = int(vote[0].getText().replace(' points', ''))
            if votes > 99:
                hn.append({'title': title, 'link': href, 'votes': votes})

    return hn


# Sort stories by votes function
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


# Declare the empty list
hn = []

# Loop through the first 10 pages of Hacker News
for i in range(1, 11):
    url = 'https://news.ycombinator.com/news?p=' + str(i)
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    links = soup.select('.titlelink')
    subtext = soup.select('.subtext')

    create_custom_hn(links, subtext)

# Create the Data Frame
df = pd.DataFrame.from_dict(sort_stories_by_votes(hn))
df.columns = df.columns.str.capitalize()

# Save the output to a CSV
csv_string = (
    'news_csvs/news_list_' +
    datetime.now().strftime("%Y_%m_%d_%H-%M-%S") +
    '.csv'
)
df.to_csv(csv_string)
