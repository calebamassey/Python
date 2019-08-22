#! python3
# readCensusExcel.py tabulates population and number of census tracts
# for each county.

import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countryData = {}

# Fill in countyData with each county's population and tracts.
print('Reading rows...')
for row in range(2, sheet.get_highest_row() + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

# Open a new text file and write the contents of countyData to it.
for row in range(2, sheet.get_highest_row() + 1):
    # Each row in the spreadsheet 