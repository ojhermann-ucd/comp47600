# imports
import a
import glob



# BOOLEAN
def tf_boolean_dict(token_list):
	"""
	This function turns a token_list into a dictionary that counts the occurances of tokens
	- key: token
	- value: (count of token in the token_list, count of all words)
	"""
	# create the dictionary shell
	boolean_dict = dict()
	# count variable
	count = 0
	# iterate over the tokens in token_list
	for token in token_list:
		# increment count
		count += 1
		# incremenet if already in the dict
		if token in boolean_dict:
			boolean_dict[token] += 1
		# create an entry if not in the list
		else:
			boolean_dict[token] = 1
	# frequency dict
	frequency_dict = boolean_dict
	for token in frequency_dict:
		frequency_dict[token] = float(boolean_dict[token] / count)
	# return
	return [boolean_dict, frequency_dict]



if __name__ == '__main__':
	print("")
	print("Boolean TF Scores")
	# go to the files
	a.go_a_to_tweets()
	# iterate over all the files
	for file_name in glob.glob("*.tweet"):
		print("File: {}".format(file_name)) # print the file name
		token_list = a.tokenize_text_file_remove_stop_words(file_name) # generate the token_list
		print("Token List: {}".format(token_list))
		boolean_outputs = tf_boolean_dict(token_list)
		print("TF Boolean Frequencies: {}".format(boolean_outputs[1]))
		print("")