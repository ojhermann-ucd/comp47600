# imports
import glob
import q1

if __name__ == "__main__":

	# go to the files
	q1.go_a_to_tweets()

	print("")
	print("TD-IDF Score Matrix")
	test_matrix_2 = q1.tf_idf_matrix()
	q1.print_matrix(test_matrix_2)

	# WORDCLOUD INPUT
	print("")
	print("TF-IDF Score Wordcloud Input")
	input_dict = q1.get_terms()
	td_idf_boolean_dict = q1.td_idf_boolean(input_dict, 2)
	word_cloud_input = q1.word_cloud_input(td_idf_boolean_dict)
	print(word_cloud_input)