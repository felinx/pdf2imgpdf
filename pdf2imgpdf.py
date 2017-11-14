# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 feilong.me All rights reserved.
#
# @author: Felinx Lee <felinx.lee@gmail.com>
# Created on Nov 13, 2017
#

import os
import io
import uuid
import logging
from tornado.options import options, define, parse_command_line
from tornado import escape

from PyPDF2 import PdfFileReader, PdfFileWriter
from wand.image import Image
import img2pdf


define("src", "/tmp/demo.pdf", type=str, help="The source PDF filename")
define("dest", "/tmp/demo_converted.pdf", type=str,
       help="The destination PDF filename")


def convert(src, dest):
    # specify paper size (A4)
    src = escape.to_unicode(src)
    dest = escape.to_unicode(dest)

    a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
    layout_fun = img2pdf.get_layout_fun(a4inpt)

    src_pdf = PdfFileReader(src)
    num_pages = src_pdf.getNumPages()

    imgs = []
    with open(dest, "w") as des_pdf:
        for i in xrange(num_pages):
            filename = "/tmp/page-%s-%s.png" % (i + 1, uuid.uuid4().hex)
            imgs.append(filename)

            pdf2img(src_pdf, i, filename)

        des_pdf.write(img2pdf.convert(imgs, layout_fun=layout_fun))

        for filename in imgs:
            os.remove(filename)

    logging.info("%s converted to %s !" % (src, dest))


def pdf2img(src_pdf, pagenum=0, filename="filename", resolution=600):
    dst_pdf = PdfFileWriter()
    dst_pdf.addPage(src_pdf.getPage(pagenum))

    pdf_bytes = io.BytesIO()
    dst_pdf.write(pdf_bytes)
    pdf_bytes.seek(0)

    with Image(file=pdf_bytes, resolution=resolution) as img:
        img.convert("png")
        img.save(filename=filename)


if __name__ == '__main__':
    parse_command_line()
    convert(options.src, options.dest)
