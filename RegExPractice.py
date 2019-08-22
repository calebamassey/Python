import re

zipcode = re.compile(r'\d{5}')

test = zipcode.search('The zipcode is 22030.')

print(test.group())