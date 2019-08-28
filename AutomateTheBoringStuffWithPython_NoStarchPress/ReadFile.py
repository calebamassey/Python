print('-------------------------------')

helloFile = open('c:\\Code\\Python\\GitHub Repo\\Python-master\\hello.txt')

helloContent = helloFile.read()

print(helloContent)

print('-------------------------------')

sonnetFile = open('c:\\Code\\Python\\GitHub Repo\\Python-master\\sonnet29.txt')

print(sonnetFile.readlines())

print('-------------------------------')

baconFile = open('c:\\Code\\Python\\GitHub Repo\\Python-master\\bacon.txt', 'w')

baconFile.write('Hello world!\n')
baconFile.close()

#Appends this write to the end of bacon.txt
baconFile = open('c:\\Code\\Python\\GitHub Repo\\Python-master\\bacon.txt', 'a')
baconFile.write('Bacon is not a vegatable.')
baconFile.close()

baconFile = open('c:\\Code\\Python\\GitHub Repo\\Python-master\\bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

print('-------------------------------')