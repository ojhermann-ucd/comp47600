# imports
import a
import b_tf
import glob
import math



# IDF NUMERATOR
def get_idf_numerator():
	# return number of files sourced
	return round(float(len(b_tf.get_file_names())), 2)




# IDF DENOMINATOR
def get_idf_denominator(term, term_dict):
	return round(float(1 + len(term_dict[term])), 2) # 1 to void zero denominator



# IDF
def get_idf(term, term_dict, base, idf_numerator):
	idf_denominator = get_idf_denominator(term, term_dict)
	return round(float(math.log(idf_numerator/idf_denominator, base)), 2)



# IDF
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

def idf(term, base, idf_numerator):
	fraction = idf_numerator / idf_denominator(term)
	return math.log(fraction, base)

def tf_idf_boolean(token_list, term, base):
	boolean_dict = b_tf.tf_boolean_dict(token_list)[1]
	tf_idf_boolean_dict = dict()
	for term in boolean_dict:
		tf_idf_boolean_dict[ter] = boolean_dict[term] * idf(term, base)
	return tf_idf_boolean_dict

def tf_idf_log_scaled(token_list, term, base):
	log_scaled_dict = b.tf_log_scaled(token_list, base)
	tf_idf_log_scaled_dict = dict()
	for term in log_scaled_dict:
		tf_idf_log_scaled_dict[ter] = log_scaled_dict[term] * idf(term, base)
	return tf_idf_log_scaled_dict

def tf_idf_augmented_frequency(token_list, term, base):
	augmented_dict = b.tf_log_scaled(token_list, base)
	tf_idf_augmented_frequency_dict = dict()
	for term in augmented_dict:
		tf_idf_augmented_frequency_dict[ter] = augmented_dict[term] * idf(term, base)
	return tf_idf_augmented_frequency_dict





if __name__ == "__main__":
	# data
	term_dict = b_tf.get_terms()

	# idf_numerator
	idf_numerator = get_idf_numerator()

	# idf_denominator
	print("")
	print("IDF Denominator")
	for t in term_dict:
		print("Term: {}".format(t))
		print("IDF Numerator: {}".format(idf_numerator))
		print("IDF Denominator: {}".format(get_idf_denominator(t, term_dict)))
		print("IDF: {}".format(get_idf(t, term_dict, 2, idf_numerator)))
		print("")

	# 