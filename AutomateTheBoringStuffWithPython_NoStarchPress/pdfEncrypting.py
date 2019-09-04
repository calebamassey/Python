import PyPDF2
pdfFile = open('C:\\Code\\Python\\AutomateTheBoringStuffWithPython_NoStarchPress\\meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter= PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('swordfish')
resultPdf = open('C:\\Code\\Python\\AutomateTheBoringStuffWithPython_NoStarchPress\\encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()