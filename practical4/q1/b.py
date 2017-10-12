# imports
import glob
import q1



if __name__ == "__main__":
	
	# go to the files
	q1.go_a_to_tweets()
	
	# TF SCORE MATRIX FOR REVIEW
	print("")
	print("TF Score Matrix")
	test_matrix = q1.create_tf_matrix()
	q1.print_matrix(test_matrix)
	print("")

	print("")
	print("TD-IDF Score Dictionary")
	term_dict = q1.get_terms()
	td_idf_boolean_dict = q1.td_idf_boolean(term_dict, 2)
	print(td_idf_boolean_dict)