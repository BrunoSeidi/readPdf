import PyPDF2

pdf_file = open('pdf.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdf_file)
total = len(pdfReader.pages)

for page_number in range(total):
    pageObj = pdfReader.pages[page_number]
    print(pageObj.extract_text())

pdf_file.close()
