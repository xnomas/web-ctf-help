#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

class Scripts:
	def __init__(self, re):
		self.re = re
		self.source_list = self.find_srcs(re)

	def print(self):
		print("""\n=============\nSCRIPTS\n=============\n""")

		i = 0
		for src in self.source_list:
			i += 1
			print(f"[+] {str(i)} : {src}")

	def find_srcs(self, re):
		soup = BeautifulSoup(re, 'html.parser')
		
		scripts = soup.find_all('script')
		
		source_list = [] 
		for s in scripts:
			if s.has_attr("src"):
				source_list.append(s["src"])
		
		return source_list