from bs4 import BeautifulSoup
import re # regex

class Flag:
	def __init__(self, request, pattern):
		self.request = request
		self.pattern = pattern
		self.flags = self.find_flag(request, pattern)

	def print(self):
		print("""\n=============\nHIDDEN FLAGS\n=============\n""")

		i = 0
		for f in self.flags:
			i += 1
			print(f'[+] {i} : {f}')

	def find_flag(self, request, pattern):
		soup = BeautifulSoup(request, 'html.parser')
		# find the flag according to pattern
		found = soup.body.find_all(text=re.compile('^'+pattern+'{\w*\W*}'))

		return  found