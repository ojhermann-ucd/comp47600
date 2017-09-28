# imports
import q1_functions


if __name__ == "__main__":

	# text file
	text_file = "q1_a.txt"
	
	# generate the tokens
	tokens = q1_functions.tokenize_text_file(text_file)
	
	# display tokens
	print("")
	print("Results of tokenizing q1.txt")
	print(tokens)