
class Cookies:
	def __init__(self, cookie_string):
		self.cookie_string = cookie_string
		self.cookie_dict = self.serialize_cookie(self.cookie_string)

	def print(self):
		print("==============\nUsing cookies:\n==============\n ")
		
		for key in self.cookie_dict:
			print(f'[+] {key} = {self.cookie_dict[key]}')

	def get_dict(self):
		return self.cookie_dict

	def serialize_cookie(self, cookie_string):
		first_split = cookie_string.split(";")
		cookie_dict = {}

		for cookie in first_split:
			part = cookie.split("=")
			cookie_dict[part[0]] = part[1]

		return cookie_dict
