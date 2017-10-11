# imports
import a
import b_tf
import glob
import math



# IDF
# idf numerator
def get_idf_numerator():
	# return number of files sourced
	return round(float(len(b_tf.get_file_names())), 2)

# idf denominator
def get_idf_denominator(term, term_dict):
	return round(float(1 + len(term_dict[term])), 2) # 1 to void zero denominator

# idf
def get_idf(term, term_dict, base, idf_numerator):
	idf_denominator = get_idf_denominator(term, term_dict)
	return round(float(math.log(idf_numerator/idf_denominator, base)), 2)



# TF-IDF
def td_idf_boolean(token_list, term_dict, base, idf_numerator):
	boolean_outputs = b_tf.tf_boolean_dict(token_list)[1]
	td_idf_dict = dict()
	for term in boolean_outputs:
		td_idf_dict[term] = boolean_outputs[term] * get_idf(term, term_dict, base, idf_numerator)
	return td_idf_dict





if __name__ == "__main__":
	# data
	term_dict = b_tf.get_terms()
	idf_numerator = get_idf_numerator()
	base = 2

	# idf_denominator
	print("")
	print("IDF Denominator")
	for t in term_dict:
		print("Term: {}".format(t))
		print("IDF Numerator: {}".format(idf_numerator))
		print("IDF Denominator: {}".format(get_idf_denominator(t, term_dict)))
		print("IDF: {}".format(get_idf(t, term_dict, 2, idf_numerator)))
		print("")

	# td_idf_boolean
	print("")
	print("TD-IDF Boolean")
	# go to the directory
	a.go_a_to_tweets()
	# iterate over the files
	for file_name in glob.glob("*.tweet"):
		# data
		token_list = a.tokenize_text_file_remove_stop_words(file_name)
		boolean_outputs = b_tf.tf_boolean_dict(token_list)
		log_scaled_dict = b_tf.tf_log_scaled(token_list, 2)
		augmented_dict = b_tf.tf_augmented_frequency(token_list)

		# boolean
		td_idf_boolean_dict = td_idf_boolean(token_list, term_dict, base, idf_numerator)
		print(td_idf_boolean_dict)