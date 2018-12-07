#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from settings import *
from pdf import *
from reportlab.pdfgen import canvas
from settings import *
'''
def main():
	setting=Settings()
	new_pdf = PDF(setting)
	new_pdf.content.setFont("Helvetica",14)
	new_pdf.content.drawString(setting.inch,setting.inch,"Hello,World")
	new_pdf.content.drawRightString(2*setting.inch,2*setting.inch,"Hello,World")
	new_pdf.content.drawCentredString(3*setting.inch,3*setting.inch,"Hello,World")
	new_pdf.content.setAuthor('Robert')
#	new_pdf.content.addOutlineEntry("Hello,World","2", level=0, closed=None)
#	new_pdf.content.showOutline()
	new_pdf.content.setStrokeColorRGB(0.2,0.5,0.3)
 	new_pdf.content.setFillColorRGB(1,0,1)
	new_pdf.content.line(100,100,0,1.7*setting.inch)
 	new_pdf.content.line(110,110,1*setting.inch,0)
	new_pdf.content.grid([100,200],[300,400,500,600])
	new_pdf.content.rect(410,410,10,10,stroke=1,fill=0)
	new_pdf.content.setTitle("agahewhgwgw")
	new_pdf.content.setSubject("hawgawgawgwgwfg")
	new_pdf.content.beginForm("fds")
	new_pdf.content.drawString(20,20,"Hello,World")
	new_pdf.content.endForm()
	new_pdf.content.doForm("fds")
	new_pdf.content.showPage()
	new_pdf.content.save()

if __name__ == "__main__":
    main()
    '''
def main():
	content = []
	setting=Settings()
	doc_instance=DOC(setting)
#add some flowables
	content.append(Paragraph(u"这是标题This is a Heading",doc_instance.styleH))
	content.append(Paragraph("This is a paragraph in <i>Normal</i> style.",doc_instance.styleN))
	doc_instance.generate_pdf()
	doc_instance.doc.build(content)


if __name__ == "__main__":
    main()
  
