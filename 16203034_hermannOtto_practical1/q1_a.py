# imports
import nltk



def tokenize_text_file(file_name):
	"""
	This function generates a token list based on a file input
	"""
	# open the text file that will be tokenized
	with open(file_name, "r") as source:
		# return the tokens generated by reading the source file
		return nltk.word_tokenize(source.read())



if __name__ == "__main__":

	# text file
	text_file = "q1_a.txt"
	
	# generate the tokens
	tokens = tokenize_text_file(text_file)
	
	# display tokens
	print("")
	print("Results of tokenizing q1.txt")
	print(tokens)