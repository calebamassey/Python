import os

os.chdir('C:\\Code\\Python')

import census2010

print (census2010.allData['AK']['Anchorage'])

ancheragePop = census2010.allData['AK']['Anchorage']['pop']
print ('The 2010 population of Anchorage was ' + str(ancheragePop))
