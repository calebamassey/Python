import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))

print(wb.get_sheet_names())

sheet = wb.get_sheet_names('Sheet3')
print(sheet)
print(sheet.title)

anotherSheet = wb.get_active_sheet()
print(anotherSheet)