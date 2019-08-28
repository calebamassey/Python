import openpyxl

# Create a new Workbook
wb = openpyxl.Workbook()
print ('New Workbook Sheet Name is: ', wb.get_sheet_names())

# Get Active Sheet in WB and edit the title
sheet = wb.get_active_sheet()
print ('New Active Sheet Title is: ', sheet.title)
sheet.title = 'Spam Bacon Eggs Sheet'
print ('New Sheet Name: ', wb.get_sheet_names())

# Save Excel Workbook
wb.save('practiceExcelWB.xlsx')