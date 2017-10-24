# imports
import nltk
from nltk.corpus import stopwords
import math



# TOKENIZE FUNCTIONS
def tokenize_string(this_string):
	return nltk.word_tokenize(this_string)

def tokenize_string_remove_stop_words(this_string):
	tokens = tokenize_string(this_string)
	stop_words = set(stopwords.words('english'))
	return [t for t in tokens if t not in stop_words]



# TF SCORES
def tf_boolean(this_string):
	token_list = tokenize_string_remove_stop_words(this_string)
	frequency_dict = dict()
	# populate frequency_dict
	for token in token_list:
		if token in frequency_dict:
			frequency_dict[token] += 1
		else:
			frequency_dict[token] = 1
	# return frequency_dict
	return frequency_dict



# IDF SCORES
def get_terms(document_list):
	# term_dict
	term_dict = dict()
	# iterate over documents
	for d in document_list:
		# generate tf_boolean
		tf_boolean_dict = tf_boolean(d)
		# iterate over the terms to populate term_dict
		for term in tf_boolean_dict:
			if term in term_dict:
				if d in term_dict[term]:
					term_dict[term][d] += tf_boolean_dict[term]
				else:
					term_dict[term][d] = tf_boolean_dict[term]
			else:
				term_dict[term] = dict()
				term_dict[term][d] = tf_boolean_dict[term]
	# return
	return term_dict

# idf numerator
def get_idf_numerator(document_list):
	# return number of documents sourced
	return round(float(len(document_list)), 2)

# idf denominator
def get_idf_denominator(term, term_dict):
	return round(float(1 + len(term_dict[term])), 2) # 1 to void zero denominator

# idf
def get_idf(term, term_dict, base, idf_numerator):
	idf_denominator = get_idf_denominator(term, term_dict)
	idf_value = round(float(math.log(1 + (idf_numerator/idf_denominator), base)), 2) # preventing negative values
	return idf_value 

# idf_boolean
def tf_idf_boolean(document_list, term_dict, base):
	# data
	idf_numerator = get_idf_numerator(document_list)
	# create the return object
	tf_idf_boolean_dict = term_dict
	# populate the return object
	for term in tf_idf_boolean_dict:
		# data
		idf = get_idf(term, term_dict, base, idf_numerator)
		for document_name in tf_idf_boolean_dict[term]:
			tf_idf_boolean_dict[term][document_name] *= idf
	# return
	return tf_idf_boolean_dict