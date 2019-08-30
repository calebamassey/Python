import openpyxl

wb = openpyxl.load_workbook('C:\\Code\\Python\\AutomateTheBoringStuffWithPython_NoStarchPress\\produceSales.xlsx')
sheet = wb.active

sheet.freeze_panes = 'A2'

wb.save('C:\\Code\\Python\\AutomateTheBoringStuffWithPython_NoStarchPress\\freezeExample.xlsx')