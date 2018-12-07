#!/usr/bin/env python
#coding=utf-8
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.pagesizes import letter,A4
from reportlab.platypus import Paragraph, BaseDocTemplate,PageTemplate,Frame
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics,ttfonts
from reportlab.lib import fonts


class DOC():
	def __init__(self,setting):
		pdfmetrics.registerFont(ttfonts.TTFont('song', 'C:/Windows/Fonts/simsun.ttc'))
		self.filename='report.pdf'
		self.pagesize=A4
		self.cm=cm
		self.styles = getSampleStyleSheet()
		self.styleN = self.styles['Normal']
		self.styleN.fontName ='song'
		self.styleH = self.styles['Heading1']
		self.styleH.fontName ='song'
		self.header_str=setting.doc_header
	def generate_pdf(self):
		self.doc=BaseDocTemplate(self.filename,pagesize=self.pagesize,topMargin = 05*self.cm)
		self.frame_footer = Frame(self.doc.leftMargin,self.doc.bottomMargin,self.doc.width,self.doc.height, id='normal')
		self.template = PageTemplate(id='test', frames=self.frame_footer, onPage=self.header,onPageEnd=self.footer) 
		self.doc.addPageTemplates([self.template])

	def footer(self,canvas,doc):

	    #设置页脚
	    #:param canvas:canvas类型  pdf画布
	    #:param doc:doc类型   整个pdf文件
	    #先保存当前的画布状态
		doc=self.doc
		canvas.saveState()
		#获取当前的页码
		self.pageNumber=("Page %s" %canvas.getPageNumber())
		p = Paragraph(self.pageNumber, self.styleN)
		#申请一块1cm大小的空间，返回值是实际使用的空间
		w, h = p.wrap(self.doc.width, self.doc.bottomMargin)
		#将页码放在指示坐标处
		p.drawOn(canvas,self.doc.leftMargin, h)
		canvas.restoreState()
 

	def header(self,canvas,doc):

	#设置页眉
	#:param canvas:canvas类型  pdf画布
	#:param doc:doc类型     整个pdf文件
		canvas.saveState()
		doc=self.doc
		self.header_content = Paragraph(self.header_str,self.styleN)
		w, h = self.header_content.wrap(self.doc.width, self.doc.bottomMargin)
		self.header_content.drawOn(canvas, self.doc.leftMargin, self.doc.topMargin + self.doc.height - 0.5*self.cm)
		#画一条横线                               
		canvas.line(self.doc.leftMargin,self.doc.bottomMargin+self.doc.height + 4.5*self.cm, self.doc.leftMargin+self.doc.width,\
		self.doc.bottomMargin+self.doc.height + 4.5*self.cm) 
		canvas.restoreState()
