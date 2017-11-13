pdf2imgpdf
====

A utility to covert a PDF to a new PDF which every page is an image,  so it can be displayed very well in anywhere(A utility to covert a PDF to a new PDF which every page is an image, 
so it can be displayed very well in anywhere(Especially in Kindle).

Some PDFs connot be deplayed well in Kindle, we can export to a new PDF with Mac Preview,
but Preview often hang up or crash when exporting some of them.

pdf2imgpdf converts PDF like Mac Preview.

- it converts every PDF page to PNG
- then it assembles those images to a new PDF

### Requirement:
	
	brew install imagemagick ghostscript

### Python:
	
	pip install wand PyPDF2 img2pdf tornado

### Usage:
	
	pdf2imgpdf --src="/tmp/demo.pdf" --dest="/tmp/well-converted.pdf"