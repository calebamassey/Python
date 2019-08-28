#! python3
# luckyGoogleSearch.py opens several Google Search Results in different tabs

import requests, sys, webbrowser, bs4

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

print('Googling...') # display text while downloading the Google Page
res = requests.get("http://www.google.com/search?q=" + ' '.join(sys.argv[1:]), headers=headers)
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")

linkElems = []

for link in soup.find_all('div', {'class': 'r'}):
    for url in link.find_all('a', {'class': False}):
        linkElems.append((url.get('href')))
        
numOpen = min(5, len(linkElems))

# Open a browser tab for  each result
for i in range(numOpen):
    webbrowser.open(linkElems[i])