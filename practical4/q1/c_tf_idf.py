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
	




if __name__ == "__main__":
	print(idf("songs", 2))
	print(idf("criticising", 2))