#imports
from urllib.request import urlopen
from bs4 import BeautifulSoup



def get_html(url):
	"""
	General
	- create BeautfiulSoup object
	Input
	- string representation of the url
	Outpu
	- a BeautifulSoup html object
	"""
	return BeautifulSoup(urlopen(url), "html.parser")



if __name__ == '__main__':

	# variables
	source_page = "https://leiterreports.typepad.com/blog/"
	soup_object = get_html(source_page)

	
	# display the content of the title of the blog
	print("")
	print("Title")
	for item in soup_object.find_all("title"):
		print(item.get_text()) # for each title part of the page, print the text content i.e. avoid the tags and shit

	# display the content of the body of the blog
	print("")
	print("Body")
	for item in soup_object.find_all("body"):
		print(item.get_text()) # for each body part of the page, print the text content i.e. avoid the tags and shit