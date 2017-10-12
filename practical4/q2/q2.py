# imports
import os
import glob
import nltk
from nltk.corpus import stopwords
import math



# DIRECTORY CHANGES
def go_q2_to_tweets():
	os.chdir("Tweets_no_stop")

def go_tweets_to_q2():
	os.chdir("../")



# FILE NAMES
def get_file_names():
	# file_name_list
	file_name_list = list()
	for file_name in glob.glob("*tweet"):
		file_name_list.append(file_name)
	return file_name_list



# FILE TO LIST
def file_to_list(file_name):
	with open(file_name, "r") as source:
		return source.read().split()



# LIST TO NGRAM LIST
def ngram_end(file_list, n):
	if len(file_list) < n:
		return len(file_list) - 1
	else:
		return len(file_list) - n + 1

def list_to_ngram_list(file_list, n):
	ngram_list = list()
	if len(file_list) < n:
		return [" ".join(file_list)]
	elif n == 1:
		return file_list
	else:
		for i in range(0, ngram_end(file_list, n), 1):
			ngram_list.append(file_list[i:i+n])
	return ngram_list

def ngram_list_to_string_list(ngram_list):
	if isinstance(ngram_list[0], str):
		return ngram_list
	else:
		return [" ".join(inner_list) for inner_list in ngram_list]



# FREQUENCIES
def all_terms(n):
	term_list = list()
	for file_name in glob.glob("*.tweet"):
		temp_list = file_to_list(file_name)
		temp_list = list_to_ngram_list(temp_list, n)
		temp_list = ngram_list_to_string_list(temp_list)
		for item in temp_list:
			if item not in term_list:
				term_list.append(item)
	return term_list

def combine_lists(n):
	combined_list = list()
	for file_name in glob.glob("*.tweet"):
		temp_list = file_to_list(file_name)
		temp_list = list_to_ngram_list(temp_list, n)
		combined_list += temp_list
	return ngram_list_to_string_list(combined_list)

def frequency_dict(n):
	combined_list = combine_lists(n)
	the_frequency_dict = dict()
	for term in combined_list:
		if term in the_frequency_dict:
			the_frequency_dict[term] += 1
		else:
			the_frequency_dict[term] = 1
	return the_frequency_dict

def probability_dict(n):
	the_frequency_dict = frequency_dict(n)
	total = 0
	for term in the_frequency_dict:
		total += the_frequency_dict[term]
	for term in the_frequency_dict:
		the_frequency_dict[term] = round(float(the_frequency_dict[term] / total), 2)
	return the_frequency_dict




if __name__ == '__main__':

	"""
	note to self: you're tired, but remember that order matters with ngrams e.g. mad dog vs dog mad
	"""

	go_q2_to_tweets()
	# file_name_list = get_file_names()
	# for file_name in file_name_list:
	# 	file_contents_list = file_to_list(file_name)
	# 	file_ngrams = list_to_ngram_list(file_contents_list, 1)
	# 	print(file_contents_list)
	# 	print(file_ngrams)
	# 	print("")

	print(all_terms(1))
	print("")
	print(all_terms(2))
	print("")
	print(combine_lists(1))
	print("")
	print(combine_lists(2))
	print("")
	print(frequency_dict(1))
	print("")
	print(frequency_dict(2))
	print("")
	print(probability_dict(1))
	print("")
	print(probability_dict(2))
	print("")