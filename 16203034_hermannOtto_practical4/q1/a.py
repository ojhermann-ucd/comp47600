# imports
import glob
import q1



if __name__ == "__main__":

	# got the source files
	q1.go_a_to_tweets()

	# tokenize and remove stop words for each file
	for file_name in glob.glob("*.tweet"):
		# create the token list
		token_list = q1.tokenize_text_file_remove_stop_words(file_name)
		# convert to string
		token_string = " ".join(token_list)
		# go to the folder for modifed tweets
		q1.go_tweets_to_a()
		q1.go_a_to_stop_removed()
		# save the new tokens with stop words removed
		with open(file_name, "w") as destination:
			destination.write(token_string)
		# go to the source of the tweets
		q1.go_stop_removed_to_a()
		q1.go_a_to_tweets()

	# return to the starting directory
	q1.go_tweets_to_a()