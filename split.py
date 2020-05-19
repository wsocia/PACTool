from tkinter import filedialog
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

fileDir = filedialog.askdirectory()



for filename in os.listdir(fileDir):
    pdf = PdfFileReader(fileDir + "/" + filename)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output_filename = fileDir + '/output/{}_page_{}.pdf'.format(filename, page+1)

        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)