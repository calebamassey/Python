import  PyPDF2

minutesFile = open('C:\\Code\\Python\\AutomateTheBoringStuffWithPython_NoStarchPress\\meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('C:\\Code\\Python\\AutomateTheBoringStuffWithPython_NoStarchPress\\pdfRotate.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close
minutesFile.close