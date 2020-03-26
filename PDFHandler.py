import PyPDF2

class PDFFile(object):
    def __init__(self, fileName):
        self.fileName= fileName

    def load_text_From_pdf(self):
        # creating a pdf file object
        pdfFileObj = open(self.fileName, 'rb')

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # printing number of pages in pdf file
        print(pdfReader.numPages)

        output = ''

        for i in range(0,pdfReader.numPages):
            pageObj = pdfReader.getPage(i)

            output = output + pageObj.extractText()

        pdfFileObj.close()
        return output
