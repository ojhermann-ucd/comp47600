# imports
import nltk



def tokenize_text_file(file_name):
	"""
	This function generates a token list based on a file input
	"""
	# open the text file that will be tokenized
	with open(file_name, "r") as source:
		# return the tokens generated by reading the source file
		return nltk.word_tokenize(source.read())



def review_post_tag(pos_tag_tokens):
	"""
	General
	- this function is used to evalute the output of using 
	"""
	for pair in pos_tag_tokens:
		print(pair[0])
		nltk.help.upenn_tagset(pair[1])
		print("")



if __name__ == "__main__":
	
	# normalization without stop word removal
	print("POS Tag with only normalization")
	tokens = tokenize_text_file("q1_b_normalized.txt")
	pos_tag_tokens = nltk.pos_tag(tokens)
	print(pos_tag_tokens)
	print("")
	review_post_tag(pos_tag_tokens)

	print("POS Tag with normalization and stop word removal")
	tokens = tokenize_text_file("q1_b_normalized_stop_removed.txt")
	pos_tag_tokens = nltk.pos_tag(tokens)
	print(pos_tag_tokens)
	print("")
	review_post_tag(pos_tag_tokens)