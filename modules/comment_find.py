#!/usr/bin/env python3
from bs4 import BeautifulSoup, Comment
import requests


class Comms: 
	def __init__(self, re): # needs a list of comments scraped from website
		self.re = re
		self.comments = self.find_comments(re) 
		 

	def print(self):  # 'pretty print' comments
		print("""\n=============\nCOMMENTS\n=============\n""")
		
		i = 0
		for c in self.comments:
			i += 1
			print(f"[+] {str(i)} :  {c}")

	def find_comments(self, re): # scrape for comments in given html response
		soup = BeautifulSoup(re, 'html.parser')

		comment_list = soup.find_all(string=lambda text: isinstance(text, Comment))

		return comment_list
