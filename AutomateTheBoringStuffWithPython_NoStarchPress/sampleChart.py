import openpyxl
from openpyxl.chart import BarChart, Reference, Series

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(1,11): # Create some data in column A
    sheet['A' + str(i)] = i

refObj = Reference(sheet, min_col=1, min_row=1, max_col=10, max_row=1)

seriesObj = Series(refObj, title='First Series')

chartObj = BarChart()
chartObj.append(seriesObj)
chartObj.top = 50 # set position
chartObj.left = 100
chartObj.width = 10 # set the size
chartObj.height = 6

sheet.add_chart(chartObj)
wb.save('C:\\Code\\Python\\AutomateTheBoringStuffWithPython_NoStarchPress\\sampleChart.xlsx')