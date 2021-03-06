# imports
import nltk
from nltk.stem import PorterStemmer


def tokenize_text_file(file_name):
	"""
	This function generates a token list based on a file input
	"""
	# open the text file that will be tokenized
	with open(file_name, "r") as source:
		# return the tokens generated by reading the source file
		return nltk.word_tokenize(source.read())



def porter_stemmer(tokens):
	"""
	General
	- this function converts the PorterStemmer() results into a readable dictionary object
	Input
	- tokens: results of tokenize_text_file()
	Output
	- Python-dictionary
	-- key: stem
	-- value: list of tokens converted into the stem
	"""
	ps_dict = dict() # create a shell dictionary
	for t in tokens: # iterate over the tokens
		t_stem = PorterStemmer().stem(t)
		if t_stem in ps_dict:
			ps_dict[t_stem].append(t) # append a list
		else:
			ps_dict[t_stem] = [t] # create a list
	return ps_dict



if __name__ == '__main__':
	
	# tokenize the text file
	text_file = "q2_a.txt"
	tokens = tokenize_text_file(text_file)

	# stem using Porter Stemming
	ps_dict = porter_stemmer(tokens)
	
	# display the Porter Stemming results in a nice way
	print("")
	print("Porter Stemming Results")
	for key in ps_dict:
		print(key)
		print(ps_dict[key])
		print("")