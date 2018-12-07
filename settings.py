#!/usr/bin/env python
#coding=utf-8
import platform

class Settings():
	def __init__(self):
		self.os_type = platform.uname()[0]

		self.doc_header="某某某某项目"
