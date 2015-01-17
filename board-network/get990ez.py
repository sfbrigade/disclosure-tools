from pyPdf import PdfFileWriter, PdfFileReader

def main():
	input1 = PdfFileReader(file("data/990EZ/943106147_2012_09da16e1.PDF", "rb"))
	output = PdfFileWriter()

	numPages = input1.getNumPages()
	print "document has %s pages." % numPages

	page = input1.getPage(1)
	print page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y()
	page.cropBox.lowerLeft = (43, 54)
	page.cropBox.upperRight = (264, 325)
	output.addPage(page)

	outputStream = file("out.pdf", "wb")
	output.write(outputStream)
	outputStream.close()

if __name__ == '__main__':
	main()