# imports
import nltk
import q1_functions



if __name__ == "__main__":
	tokens = q1_functions.tokenize_text_file("q1_b.txt")
	pos_tag_tokens = nltk.pos_tag(tokens)
	print(pos_tag_tokens)

	print("")
	q1_functions.review_post_tag(pos_tag_tokens)