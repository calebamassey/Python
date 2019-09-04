import docx

doc = docx.Document()

doc.add_picture('C:\\Code\\Python\\AutomateTheBoringStuffWithPython_NoStarchPress\\zophie.png', width=docx.shared.Inches(1), height=docx.shared.Cm(4))
doc.save('C:\\Code\\Python\\AutomateTheBoringStuffWithPython_NoStarchPress\\image.docx')4