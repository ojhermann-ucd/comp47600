# imports
import a
import glob
import math



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
		frequency_dict[token] = round(float(boolean_dict[token] / count), 2)
	# return
	return [boolean_dict, frequency_dict]



# LOG-SCALED
def tf_log_scaled(token_list, base):
	"""
	This function turns the boolean frequncy and transforms it into a log-scaled frequency
	"""
	log_scaled_outputs = tf_boolean_dict(token_list)
	for token in log_scaled_outputs[1]:
		log_scaled_outputs[1][token] = round(math.log(log_scaled_outputs[1][token], base),2)
	return log_scaled_outputs



# Augmented frequency




if __name__ == '__main__':
	# go to the files
	a.go_a_to_tweets()
	# iterate over all the files
	for file_name in glob.glob("*.tweet"):
		# generate the data
		token_list = a.tokenize_text_file_remove_stop_words(file_name)
		boolean_outputs = tf_boolean_dict(token_list)
		log_scaled_outputs = tf_log_scaled(token_list, 2)

		# general information
		print("")
		print("File: {}".format(file_name)) # print the file name
		print("Token List: {}".format(token_list))

		# boolean
		print("TF Boolean Frequencies: {}".format(boolean_outputs[1]))

		# log scaled
		print("TF Log-Scaled Frequencies: {}".format(log_scaled_outputs[1]))

		# augmented frequncy