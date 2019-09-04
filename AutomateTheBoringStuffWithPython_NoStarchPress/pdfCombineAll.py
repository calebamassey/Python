#! python3
# pdfCombineAll.py - Combines all the PDFS in the current working directory
# into a single PDF.

import PyPDF2, os

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.\\AutomateTheBoringStuffWithPython_NoStarchPress'):
    if filename.endswith('.pdf'):
        if (filename != 'encryptedminutes.pdf'):
            pdfFiles.append('C:\\Code\\Python\\AutomateTheBoringStuffWithPython_NoStarchPress\\' + filename)
pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open (filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through  all the pages (except  the first) and add them.
    for pageNum in range (1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('C:\\Code\\Python\\AutomateTheBoringStuffWithPython_NoStarchPress\\allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()