#imports
from urllib.request import urlopen
from bs4 import BeautifulSoup



def get_html(url):
	return BeautifulSoup(urlopen(url), "html.parser")



if __name__ == '__main__':

	# variables
	source_page = "https://leiterreports.typepad.com/blog/"
	soup_object = get_html(source_page)

	
	# display the content of the title of the blog
	print("")
	print("Title")
	for item in soup_object.find_all("title"):
		print(item.get_text())

	# display the content of the body of the blog
	print("")
	print("Body")
	for item in soup_object.find_all("body"):
		print(item.get_text())