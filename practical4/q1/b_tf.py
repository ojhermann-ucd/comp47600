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
	log_scaled_dict = tf_boolean_dict(token_list)[0]
	for token in log_scaled_dict:
		log_scaled_dict[token] = round(math.log(log_scaled_dict[token], base),2)
	return log_scaled_dict



# AUGMENTED FREQUENCY
def max_value_in_dict(this_dict):
	maximum_value = 0
	for key in this_dict:
		maximum_value = max(maximum_value, this_dict[key])
	return maximum_value

def tf_augmented_frequency(token_list):
	boolean_outputs = tf_boolean_dict(token_list) 
	augmented_dict = tf_boolean_dict(token_list)[0]
	maximum_token_count = max_value_in_dict(boolean_outputs[0])
	for token in augmented_dict:
		augmented_dict[token] = round(0.5 + (0.5 * augmented_dict[token]) / maximum_token_count, 2)
	return augmented_dict



# MATRIX
def get_terms():
	# got to tweets
	a.go_a_to_tweets()
	# create terms_dict
	terms_dict = dict()
	# iterate over the tweet files
	for file_name in glob.glob("*tweet"):
		# generate the data
		token_list = a.tokenize_text_file_remove_stop_words(file_name)
		boolean_outputs = tf_boolean_dict(token_list)[0]
		# populate terms_dict
		for key in boolean_outputs:
			if key not in terms_dict:
				terms_dict[key] = dict()
				terms_dict[key][file_name] = 1
			else:
				if file_name not in terms_dict[key]:
					terms_dict[key][file_name] = 1
				else:
					terms_dict[key][file_name] += 1
	a.go_tweets_to_a()
	return terms_dict

	# return
	return terms_dict

def get_file_names():
	a.go_a_to_tweets()
	file_list = [file_name for file_name in glob.glob("*.tweet")]
	a.go_tweets_to_a()
	return file_list

def get_matrix():
	# print the file names
	file_names = get_file_names()
	# get terms
	terms_dict = get_terms()
	# return
	return [file_names, terms_dict]

def print_matrix():
	# data
	matrix_data = get_matrix()
	file_names = matrix_data[0]
	terms_dict = matrix_data[1]
	# PRINTING
	print_list = list()
	# file names
	file_print = file_names
	file_print.insert(0, "")
	print_list.append(file_print)
	# terms
	for t in terms_dict:
		temp_list = list()
		temp_list.append(t)
		for f in file_names[1::1]:
			if f in terms_dict[t]:
				temp_list.append(terms_dict[t][f])
			else:
				temp_list.append(0)
		print_list.append(temp_list)
	# print
	for item in print_list:
		print(" ".join(["{:>16}".format(f) for f in item]))



if __name__ == '__main__':
	
	# go to the files
	a.go_a_to_tweets()
	# iterate over all the files
	for file_name in glob.glob("*.tweet"):
		# generate the data
		token_list = a.tokenize_text_file_remove_stop_words(file_name)
		boolean_outputs = tf_boolean_dict(token_list)
		log_scaled_dict = tf_log_scaled(token_list, 2)
		augmented_dict = tf_augmented_frequency(token_list)

		# general information
		print("")
		print("")
		print("File: {}".format(file_name)) # print the file name
		print("")
		print("Token List: {}".format(token_list))
		print("")
		# boolean
		print("TF Boolean Frequencies: {}".format(boolean_outputs[1]))
		print("")
		# log scaled
		print("TF Log-Scaled Frequencies: {}".format(log_scaled_dict))
		print("")
		# augmented frequncy
		print("TF Augmented Frequencies: {}".format(augmented_dict))
		print("")
	# go back to the starting diectory
	a.go_tweets_to_a()

	# matrix
	print_matrix()
