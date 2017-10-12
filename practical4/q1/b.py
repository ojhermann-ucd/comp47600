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

	# WORDCLOUD INPUT
	print("")
	print("TF Score Wordcloud Input")
	input_dict = q1.get_terms()
	word_cloud_input = q1.word_cloud_input(input_dict)
	print(word_cloud_input)