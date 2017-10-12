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
	print("TD-IDF Score Matrix")
	test_matrix_2 = q1.tf_idf_matrix()
	q1.print_matrix(test_matrix_2)