#! python3
# luckyGoogleSearch.py opens several Google Search Results in different tabs

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google Page
res = requests.get("https://www.google.com/search?q=" + ' '.join(sys.argv[1:]))
res.raise_for_status()
#webbrowser.open("https://www.google.com/search?q=" + ' '.join(sys.argv[1:]))
# Retrieve  top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open a browser tab for  each result.
linkElems = soup.select('.r a')
print(linkElems)
numOpen = min(5, len(linkElems))
print (numOpen)
for i in range(numOpen):
    print(i)
    webbrowser.open(linkElems[i].get('href'))
