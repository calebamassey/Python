import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('C:\\Code\\Python\\AutomateTheBoringStuffWithPython_NoStarchPress\\encrypted.pdf', 'rb'))
print ('PDF Encrypted: ', pdfReader.isEncrypted)

#pdfReader.getPage(0)
pdfReader.decrypt('rosebud')
print ('Get Page: \n', pdfReader.getPage(0))