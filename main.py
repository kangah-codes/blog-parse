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
		return re.sub(r'!(h\d){(.*)}', r'<\1>\2</\1>', text)


	def parse_paragraphs(self, text):
		return re.sub(r'!p{(.*)}', r'<p>\1</p>', text)

	def parse_quotes(self, text):
		return re.sub(r'!quote_(h\d){(.*)}', r'<blockquote><\1>\2</\1></blockquote>', text)

	def parse_tables(self, text):
		pass


a = """
!h5{Hello my guy} 
!h2{lmao} 
!h7{sdfa}

!p{The last thing}

!quote_h6{LMAO}

"""

p = Parser(a)

print(p.parse_headings(a))
print(p.parse_paragraphs(a))
print(p.parse_quotes(a))


							
