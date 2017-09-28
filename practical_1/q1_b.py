# imports
from nltk.corpus import stopwords
import q1_functions
import q1_spell_checker



if __name__ == "__main__":

	# variables
	text_file = "q1_a.txt"
	dv_us = "en_US"
	dv_uk = "en_UK"
	pwl = "q1_spell_checker_personal_dictionary.txt"
	text  = open(text_file).read()
	dv_list = [dv_us, dv_uk]

	# spell check: not requested, but something I'd include as part of my process
	print("")
	print("Otto, in the report remember to explain why you used both a UK and US dictionary.")
	print("")
	print(text)
	new_text = q1_spell_checker.corrections_and_amendments(q1_spell_checker.spell_checker_q1_mutiple_languages(dv_list, pwl, text), text, pwl).lower()
	with open("q1_b.txt", "w") as destination:
		# save the file after all the changes: spell checked and lower case
		destination.write(new_text)

	# removing stop words: not strictly part of normalization, but could be; at any rate, it's something I would do in the first instance unless I had compelling reasons not to remove stop words
	stop_words = set(stopwords.words('english'))
	new_text = [word for word in new_text.strip().split() if word not in stop_words]
	new_text = " ".join(new_text)
	with open("q1_b.txt", "w") as destination:
		destination.write(new_text)

	# display the new tokens
	new_tokens = q1_functions.tokenize_text_file("q1_b.txt")
	print(new_tokens)