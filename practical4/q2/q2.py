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



# PMI
def pmi_score(p_combined, p_1, p_2):
	denominator = float(p_1 * p_2)
	fraction = float(p_combined / denominator)
	return math.log(fraction, 2)

def pmi_score_dict_for_2():
	# data
	bigram_dict = probability_dict(2)
	unary_dict = probability_dict(1)
	the_pmi_score_dict = dict()
	# populate the_pmi_score_dict
	for bigram in bigram_dict:
		# terms
		bi_1 = bigram.split()[0]
		bi_2 = bigram.split()[1]
		# probabilities
		p_combined = bigram_dict[bigram]
		p_1 = unary_dict[bi_1]
		p_2 = unary_dict[bi_2]
		# add the pmi to the dictionary
		the_pmi_score_dict[bigram] = round(float(pmi_score(p_combined, p_1, p_2)),2)
	# return
	return the_pmi_score_dict



# TOP TEN
def merge_dict(d1, d2):

	# create the return object 
	d = {}

	# get smallest elements until one dict is empty
	while len(d1) > 0 and len(d2) > 0:

		# create the traverse objects
		d1_v, d2_v = next(iter(d1)), next(iter(d2))

		# put the larger score into the return dictionary
		if d1[d1_v] > d2[d2_v]:
			d[d1_v] = d1[d1_v]
			del d1[d1_v]
		else:
			d[d2_v] = d2[d2_v]
			del d2[d2_v]

	# add remaining elements
	while len(d1) > 0:
		d1_v = next(iter(d1))
		d[d1_v] = d1[d1_v]
		del d1[d1_v]
	while len(d2) > 0:
		d2_v = next(iter(d2))
		d[d2_v] = d2[d2_v]
		del d2[d2_v]

	# return
	return d

def merge_sort_dict(d):

	# objects
	d1 = {}
	d2 = {}
	length = len(d)
	middle = int(length / 2)

	if len(d) > 1:
		for i in range(0, middle, 1):
			next_item = next(iter(d))
			d1[next_item] = d[next_item]
			del d[next_item]

		for i in range(middle, length, 1):
			next_item = next(iter(d))
			d2[next_item] = d[next_item]
			del d[next_item]

		d1 = merge_sort_dict(d1)
		d2 = merge_sort_dict(d2)
		d = merge_dict(d1, d2)
	
	return d

def top_ten(d):
	source_dict = merge_sort_dict(d)
	if len(source_dict) < 11:
		return source_dict
	return_dict = dict()
	total = 0
	value = None
	while total < 11:
		key = next(iter(source_dict))
		value = source_dict[key]
		return_dict[key] = value
		del source_dict[key]
		total += 1
	new_value = value
	while new_value == value:
		key = next(iter(source_dict))
		new_value = source_dict[key]
		if new_value == value:
			return_dict[key] = new_value
			del source_dict[key]
	return return_dict





if __name__ == '__main__':

	"""
	note to self: you're tired, but remember that order matters with ngrams e.g. mad dog vs dog mad
	"""

	# go to the file
	go_q2_to_tweets()

	# pmi scores
	print("")
	print("PMI Scores")
	print(pmi_score_dict_for_2())

	# pmi scores
	print("")
	print("Sorted PMI Scores")
	print(merge_sort_dict(pmi_score_dict_for_2()))

	# top ten
	print("")
	print("Top Ten PMI Scores")
	print(top_ten(pmi_score_dict_for_2()))