import requests

class Headers:
	def __init__(self, re, important_only: bool):
		self.re = re
		self.important_only = important_only
		self.headers = self.get_headers(re, important_only)

	def get_headers(self, re, important_only: bool):
		if important_only:
			headers = { h:re.get(h) for h in re if is_important_header(h)}
			return headers

		headers = {h:re.get(h) for h in re}
		return headers


	def print(self):
		if self.important_only:
			print("""\n===================\nINTERESTING HEADERS\n===================\n""")
			for h in self.headers:
				print(f'{h} : {self.headers.get(h)}')

		else: 
			print("""\n=============\nALL HEADERS\n=============\n""")			
			for h in self.headers:
				print(f'{h} : {self.headers.get(h)}')


def is_important_header(check):
	important_headers = {
	'cookie' : 1, 
	'set-cookie' : 2 ,
	'access-control-allow-origin' : 3,
	'access-control-allow-credentials' : 4,
	'access-control-allow-headers' : 5,
	'access-control-allow-methods' : 6,
	'server' : 7,
	'cross-origin' : 8,
	'content-security-policy' : 9,
	'upgrade-insecure-requests' : 10,
	'x-frame-options' : 11,
	'x-permitted-cross-domain-policies' : 12,
	'x-powered-by' : 13
	}

	if important_headers.get(check.lower()) is not None:
		return True
	return False
