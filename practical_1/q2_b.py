# imports
import nltk
from nltk.stem import WordNetLemmatizer



# resources
# http://wordnet.princeton.edu/man/wndb.5WN.html
# pos Syntactic category: n for noun files, v for verb files, a for adjective files, r for adverb files.
# https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html



def tokenize_text_file(file_name):
	"""
	This function generates a token list based on a file input
	"""
	# open the text file that will be tokenized
	with open(file_name, "r") as source:
		# return the tokens generated by reading the source file
		return nltk.word_tokenize(source.read())


def pos_conversion(pos):
	indicator = pos[0]
	if indicator == "N":
		return "n"
	elif indicator == "V":
		return "v"
	elif indicator == "J":
		return "a"
	elif indicator == "R":
		return "r"
	else:
		return None

def word_net_lemmatizer(tokens):
	# wnl_dict = dict()
	# for t in tokens:
	# 	print(t)
	# 	print(WordNetLemmatizer().lemmatize(t, pos='v'))
	# 	print("")


	pos_tag_tokens = nltk.pos_tag(tokens)
	wnl_dict = dict()
	for pair in pos_tag_tokens:
		word = pair[0]
		pos = pos_conversion(pair[1])
		key = None
		if pos is None:
			key = WordNetLemmatizer().lemmatize(word)
		else:
			key = WordNetLemmatizer().lemmatize(word, pos=pos)
		if key in wnl_dict:
			wnl_dict[key].append(word)
		else:
			wnl_dict[key] = [word]
	return wnl_dict



if __name__ == '__main__':
	
	# tokenize the text file
	text_file = "q2_a.txt"
	tokens = tokenize_text_file(text_file)

	# display the WordNet Lemmatizer results in a nice way
	print("")
	print("WordNet Lemmatizer Results")
	wnl_dict = word_net_lemmatizer(tokens)
	for key in wnl_dict:
		print(key)
		print(wnl_dict[key])
		print("")

