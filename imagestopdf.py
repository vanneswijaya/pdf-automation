from fpdf import FPDF
from PIL import Image
import os, os.path

# pdf = FPDF()
# # imagelist is the list with all image filenames
# for image in imagelist:
#     pdf.add_page()
#     pdf.image(image,x,y,w,h)
# pdf.output("yourfile.pdf", "F")

# months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

imagelist = []
for x in range(397433,397507):
    if 397464<x<397479 or 397495<x<397504:
        continue
    imagelist.append(x)


def makePdf(pdfFileName, listPages, dir = ''):
    if (dir):
        dir += "/"

    # cover = Image.open(dir + str(listPages[0]) + ".png")
    # width, height = cover.size
    # print(f'width {width}, height {height}')
    width, height = 720, 1560

    pdf = FPDF(unit = "pt", format = [width, height])

    # pdf.add_page()
    # pdf.image('LOGOCC.png', 0, 0, width, height)

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page) + ".jpg", 0, 0, width, height)

    pdf.output(dir + pdfFileName + ".pdf", "F")

# makePdf('pdftest5', imagelist, 'foto/2')
makePdf('12a6_28_vannes_edufair', imagelist)
# for month in months:
#     filelist = [name for name in os.listdir(f'Png/{month}')]
#     print(filelist)
#     dircount = len(filelist) - 1
#     print(dircount)
#     imagelist = [f'{month} {x}' for x in range(1, dircount+1)]
#     print(imagelist)
#     makePdf(month, imagelist, f'Png/{month}')