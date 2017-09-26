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

def token_dict(token_list):
	"""
	This function generates a dictionary of tokens where the key is the token and the value is the number of occurances of that token
	"""
	# genate the dictionary shell
	t_dict = dict()
	# populate t_dict
	for t in token_list:
		if t in t_dict:
			t_dict[t] += 1
		else:
			t_dict[t] = 1
	# return
	return t_dict

def lower_case_token_list(token_list):
	"""
	This function turns everything into lower case
	"""
	return [t.lower() for t in token_list]


if __name__ == "__main__":
	
	# generate the tokens
	tokens = tokenize_text_file("q1.txt")
	
	# display tokens
	print("")
	print("Results of tokenizing q1.txt")
	print(tokens)
	
	# tokens dictionary
	print("")
	print("Putting the tokens into a dictionary for easier viewing")
	print(token_dict(tokens))

	# normalisation: lower case
	print("")
	print("Normalisation: lower case")
	tokens_lower_case = lower_case_token_list(tokens)
	print(tokens_lower_case)

	# tokens_lower_case_dict
	print("")
	print("Putting the lower case tokens into a dictionary for easier viewing")
	print(token_dict(tokens_lower_case))