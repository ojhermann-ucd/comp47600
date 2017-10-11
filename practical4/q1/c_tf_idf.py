# imports
import a
import b_tf
import glob
import math



# IDF
def idf_numerator():
	return len(b_tf.get_file_names())

def idf_denominator(term):
	# go to directory
	a.go_a_to_tweets()
	# appearances
	appearances = 0
	for file_name in glob.glob("*.tweet"):
		# generate data
		token_list = a.tokenize_text_file_remove_stop_words(file_name)
		boolean_dict = b_tf.tf_boolean_dict(token_list)[0]
		# update appearances
		if term in boolean_dict:
			appearances += 1
	# go back to the starting directory
	a.go_tweets_to_a()
	# return
	return 1 + appearances

def idf(term, base):
	fraction = idf_numerator() / idf_denominator(term)
	return math.log(fraction, base)

def tf_idf_boolean(token_list, term, base):
	boolean_dict = b_tf.tf_boolean_dict(token_list)[1]
	tf_idf_dict = dict()
	for term in boolean_dict:
		tf_idf_dict[ter] = boolean_dict[term] * idf(term, base)
	return tf_idf_dict

def tf_idf_log_scaled(token_list, term, base):
	log_scaled_dict = b.tf_log_scaled(token_list, base)
	tf_idf_dict = dict()
	for term in log_scaled_dict:
		tf_idf_dict[ter] = log_scaled_dict[term] * idf(term, base)
	return tf_idf_dict

def tf_idf_augmented_frequency(token_list, term, base):
	augmented_dict = b.tf_log_scaled(token_list, base)
	tf_idf_dict = dict()
	for term in augmented_dict:
		tf_idf_dict[ter] = augmented_dict[term] * idf(term, base)
	return tf_idf_dict




if __name__ == "__main__":
	print(idf("songs", 2))
	print(idf("criticising", 2))