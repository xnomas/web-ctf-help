#!/usr/bin/env python3

from modules.comment_find import Comms
from modules.script_source_find import Scripts
from modules.img_source_find import Images
from modules.headers_view import Headers
import requests
from bs4 import BeautifulSoup, Comment
import argparse 

parser = argparse.ArgumentParser(prog="webctf")
parser.add_argument("url", help="URL to fetch info from", type=str)
parser.add_argument("-c", "--comments", help="Scrape for HTML comments on given website", action="store_true")
parser.add_argument("-sc", "--scripts", help="Scrape for script sources on given website", action="store_true")
parser.add_argument("-si", "--img", help="Scrape for all image sources on given website", action="store_true")
parser.add_argument("-he", "--headers", help="Displays response headers deemed important. To show all use '-he | --headers a'",
 					nargs="?", const="i", type=str, metavar=" a ")
parser.add_argument("-a", "--all", help="Use all options on given url. Runs with important headers. Use '-a | --all a' to show all headers",
					 nargs="?", const="i", type=str, metavar=" a ")

args = parser.parse_args()

def main():
	if args.url:
		re = requests.get(args.url)

		if args.comments:
			comments = Comms(re.text)
			comments.print()

		if args.scripts:
			scripts = Scripts(re.text)
			scripts.print()

		if args.img:
			images = Images(re.text)
			images.print()

		if args.headers == 'i':
			header = Headers(re.headers, True) # True -> only important headers
			header.print()
		elif args.headers == 'a':
			header = Headers(re.headers, False) # False -> all headers
			header.print()

		if args.all:
			comments = Comms(re.text)
			scripts = Scripts(re.text)
			images = Images(re.text)

			if args.all == "i": 
				header = Headers(re.headers, True)
			elif args.all == "a":
				header = Headers(re.headers, False)

			header.print()
			comments.print()
			scripts.print()
			images.print()




if __name__ == "__main__":
	main()
