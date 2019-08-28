import shelve

#Stores names  of cats into shelf (python storage)
shelfFile = shelve.open('mydata')
cats  = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])

shelfFile.close()