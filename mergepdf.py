import PyPDF2 

months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun']

pdf1File = open('VANNES WIJAYA_1.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)

pdfWriter = PyPDF2.PdfFileWriter()
pdf2File = open('VANNES WIJAYA_2.pdf', 'rb')
pdf3File = open('VANNES WIJAYA_3.pdf', 'rb')
pdf4File = open('VANNES WIJAYA_4.pdf', 'rb')

pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdf3Reader = PyPDF2.PdfFileReader(pdf3File)
pdf4Reader = PyPDF2.PdfFileReader(pdf4File)

page1 = pdf3Reader.getPage(1)
pdfWriter.addPage(page1)
page2 = pdf3Reader.getPage(1)
pdfWriter.addPage(page2)
page3 = pdf3Reader.getPage(1)
pdfWriter.addPage(page3)
page4 = pdf3Reader.getPage(1)
pdfWriter.addPage(page4)

# for pageNum in range(pdf1Reader.numPages):
    # if pageNum == 33:
    #     for month in months:
    #         pdf2File = open(f'Png/{month}/{month}.pdf', 'rb')
    #         pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
    #         for x in range(pdf2Reader.numPages):
    #             pageObj2 = pdf2Reader.getPage(x)
    #             pdfWriter.addPage(pageObj2)
    # if pageNum == 26:
    #     for y in range(pdf3Reader.numPages):
    #         pageObj3 = pdf3Reader.getPage(y)
    #         pdfWriter.addPage(pageObj3)
    # if pageNum == 28:
    #     for z in range(pdf4Reader.numPages):
    #         pageObj4 = pdf4Reader.getPage(z)
    #         pdfWriter.addPage(pageObj4)
    # pageObj = pdf1Reader.getPage(pageNum)
    # pdfWriter.addPage(pageObj)
 
# for pageNum in range(pdf2Reader.numPages):
#     pageObj = pdf2Reader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)

# from PyPDF2 import PdfFileWriter, PdfFileReader
# pages_to_keep = [x for x in range(0, 14)] # page numbering starts from 0
# for y in range(31, 132):
#     pages_to_keep.append(y)
# infile = PdfFileReader('jurnalfinal.pdf', 'rb')
# output = PdfFileWriter()

# print(pages_to_keep)

# for i in pages_to_keep:
#     p = infile.getPage(i)
#     output.addPage(p)

# with open('revisijurnal1.pdf', 'wb') as f:
#     output.write(f)

pdfOutputFile = open('schoolreports.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
pdf3File.close()
pdf4File.close()