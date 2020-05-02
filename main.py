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
		"""
		<table>
		<thead>
		<tr>
		<th>Name</th>
		<th>Age</th>
		</tr>
		</thead>
		<tbody>
		<tr>
		<td>Bob</td>
		<td>27</td>
		</tr>
		<tr>
		<td>Alice</td>
		<td>23</td>
		</tr>
		</tbody>
		</table>
		!table_th{Name}_th{Age}_td{Lmao}_td{Lmao}
		"""
		return re.sub(r'!table_(th{.*}){.}', r'lol', text)

	def parse_lists(self, text, typeof):
		if typeof == 'ol':
			#print(re.findall(r'!ol_li{(.*)}', text))
			print(re.sub(r'!ol_(li{(.*)})|(li{(.*)})', r'<ol><li>\2</li></ol>', text))


a = """
!ol_li{YEAH}_li{lmao}
!ol_li{OKAY}
!ol_li{lol}

"""

p = Parser(a)

print(p.parse_lists(a, 'ol'))


							
