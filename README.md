pdf2imgpdf (pdf2img then img2pdf)
====

A utility to covert a PDF to a new PDF which every page is an image,  so it can be displayed very well in anywhere(Especially in Kindle).

Some PDFs connot be deplayed well in Kindle, we can export to a new PDF with Mac Preview,
but Preview often hang up or crash when exporting some of them.

pdf2imgpdf converts PDF like Mac Preview.

- It converts every PDF page to PNG
- Then, it assembles those images to a new PDF

### Requirement:
	
	brew install imagemagick ghostscript

### Python:
	
	pip install wand PyPDF2 img2pdf tornado

### Usage:
	
	python pdf2imgpdf --src="/tmp/demo.pdf" --dest="/tmp/well-converted.pdf"

Or use pdf2imgpdf as a Python lib:

    from pdf2imgpdf import convert

    src = "/tmp/demo.pdf"
    dest = "/tmp/well-converted.pdf"

    convert(src, dest)
