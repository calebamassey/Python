import PyPDF2
pdfFileObj = open('C:\\Code\\Python\\AutomateTheBoringStuffWithPython_NoStarchPress\\meetingminutes.pdf', 'rb')
pdfReader =  PyPDF2.PdfFileReader(pdfFileObj)
print ('Number of Pages', pdfReader.numPages)

pageObj = pdfReader.getPage(0)
print('Text: ', pageObj.extractText())