# imports
import q1_functions



if __name__ == "__main__":

	# generate the tokens
	tokens = q1_functions.tokenize_text_file("q1.txt")

	# make tokens lower case
	tokens = q1_functions.lower_case_token_list(tokens)

	print(tokens)