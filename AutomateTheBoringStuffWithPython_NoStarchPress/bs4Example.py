import requests, bs4

#Open HTML File for specific URL
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(noStarchSoup))

#Open Local HTML File
exampleFile = open('C://Code//Python//GitHub Repo//Python-master//example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features="html.parser")

#Select Author  information from HTML File
elems = exampleSoup.select('#author')
print (type(elems))
print (len(elems))
print (type(elems[0]))
print (elems[0].getText())
print (str(elems[0]))  
print (elems[0].attrs)

#Select Paragraph information from HTML File
pElems = exampleSoup.select('p')
print(pElems[0])
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())

#Select Span informaton from HTML File
spanElem = exampleSoup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') == None)
print(spanElem.attrs)