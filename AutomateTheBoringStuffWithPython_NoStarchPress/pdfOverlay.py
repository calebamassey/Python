import PyPDF2
minutesFile = open('C:\\Code\\Python\\AutomateTheBoringStuffWithPython_NoStarchPress\\meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('C:\\Code\\Python\\AutomateTheBoringStuffWithPython_NoStarchPress\\watermark.pdf', 'rb'))

minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

resultPdfFile = open('C:\\Code\\Python\\AutomateTheBoringStuffWithPython_NoStarchPress\\watermarkCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close
resultPdfFile.close