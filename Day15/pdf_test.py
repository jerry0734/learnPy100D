from os import read
import PyPDF2 as pypdf2

with open("Day15\\res\\Docker.pdf", 'rb') as pdf:
    reader = pypdf2.PdfFileReader(pdf, strict=False)
    print(reader.numPages)
    if reader.isEncrypted:
        reader.decrypt('')
    current_page = reader.getPage(5)
    print(current_page)
    print(current_page.extractText())
