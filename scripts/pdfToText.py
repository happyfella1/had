import os
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

inputData = "data/data1_pdfs"
outputData = "data/data1_docs"

projectPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

inputDataPath = os.path.join(projectPath,inputData)
outputDataPath = os.path.join(projectPath,outputData)


def makeDirectory(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

allFields = os.listdir(inputDataPath)
for field in allFields:
    makeDirectory(os.path.join(outputDataPath, field))


def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text


for field in allFields:
    files = os.listdir(os.path.join(inputDataPath,field))
    for fil in files:
        x = convert(os.path.join(inputDataPath,field,fil))
        oufil = os.path.splitext(fil)[0]
        outfile = os.path.join(outputDataPath,field,oufil)
        print outfile
        f = open(outfile,'w')
        f.write(x)
        f.close()

