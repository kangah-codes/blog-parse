"""
Parser for taking text and returning html

So for instance a text like:
	!(h1)[Hello world] will return <h1>Hello world</>

"""
import re
from re import split

class Parser:
	def __init__(self, text):
		self.text = text
		self.length = len(self.text)
		self.headings = []
		self.paragraphs = []
		self.quotes = []
		self.tables = []
		self.lists = []
		self.images = []
		self.links = []

	def parse_headings(self, text):
		for i in re.findall(r'!(h\d){(.*)}', text):
			self.headings.append(f"<{i[0]}>{i[1]}</{i[0]}>")

	def parse_paragraphs(self, text):
		for i in re.findall(r'!(p){(.*)}', text):
			self.paragraphs.append(f"<{i[0]}>{i[1]}</{i[0]}>")

	def parse_quotes(self, text):
		for i in re.findall(r'!(quote){(.*)}', text):
			self.paragraphs.append(f"<blockquote><p>{i[1]}</p></blockquote>")

	def parse_tables(self, text):
		pass


a = """
!h5{Hello my guy} 
!h2{lmao} 
!h7{sdfa}

!p{The last thing}

"""

p = Parser(a)

p.parse_headings(a)
p.parse_paragraphs(a)
print(p.headings)
print(p.paragraphs)


							
