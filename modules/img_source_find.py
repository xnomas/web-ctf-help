from bs4 import BeautifulSoup
import requests

class Images:
	def __init__(self, re):
		self.re = re
		self.image_srcs = self.find_sources(re, True)
		self.image_alts = self.find_sources(re, False)

	def print(self):
		print("""\n=============\nIMAGES\n=============\n""")

		i = 0
		print("sources:\n--------")
		for img in self.image_srcs:
			i += 1
			print(f"[+] {str(i)} : {img}") 
		
		print("\nalts:\n-----")
		i = 0
		for alt in self.image_alts:
			i += 1
			print(f"[+] {str(i)} : {alt}")

	def find_sources(self, re, sources):
		soup = BeautifulSoup(re, "html.parser")

		first_img = soup.find_all("img")

		img_srcs = []

		if sources:
			for img in first_img:
				img_srcs.append(img["src"])
		else:
			for img in first_img:
				if img.has_attr("alt"):
					img_srcs.append(img["alt"])
				else:
					img_srcs.append("No alt")
		return img_srcs
