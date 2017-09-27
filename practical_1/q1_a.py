# imports
import q1_functions


if __name__ == "__main__":
	
	# generate the tokens
	tokens = q1_functions.tokenize_text_file("q1.txt")
	
	# display tokens
	print("")
	print("Results of tokenizing q1.txt")
	print(tokens)
	
	# # convert the tokens into a dictionary for easier review
	# print("")
	# print("Putting the tokens into a dictionary for easier viewing")
	# print(q1_functions.token_dict(tokens))