# imports
import enchant
from enchant.checker import SpellChecker



"""
This is quick and dirty and just made for me to do this assignment, so:
- don't expect this to scale
- don't expect this to be robust
- don't expect this to be well thought out
- it was made for this exercise and won't be used again
"""



def spell_checker_q1_single_language(dv, pwl, text):
	"""
	Inputs
	- dv: dictionary version e.g. "en_US"
	- pwl: personal word list e.g. "q1_spell_checker_personal_dictionary.txt"
	- text: text file to be spell checked
	Output
	- a Python dictionary object
	-- key: potential spelling error
	-- value: list of suggested corrections
	"""

	# Enchange dictionary objects
	my_spell_checker = SpellChecker(dv) # establish which dictionary to use when checking the text block
	my_dict = enchant.DictWithPWL(dv, pwl) # specify the dictionary to be used
	my_spell_checker.set_text(text) # load the text into my_spell_checker
	
	# Identify possible spelling errors
	possible_spelling_error_dict = dict() # create a Python-dictionary object
	for error in my_spell_checker: # iterate over the identified spelling errors
		possible_spelling_error_dict[error.word] = my_dict.suggest(error.word) # set the key to the spelling mistake and the value to the list of suggested corrections
	# Return the populated dictionary
	return possible_spelling_error_dict



def intersection_of_two_dicts(dict1, dict2):
	"""
	General
	- generate a Python dictionary from two other Python dictionaries
	- return the spelling errors common to both dictionaries
	Input
	- dict1: the return object of spell_checker_q1_single_language
	- dict2: the return object of spell_checker_q1_single_language
	Output
	- a Python dictionary object
	-- only spelling errors in common to the two inputs
	-- key: potential spelling error
	-- value: unique suggested corretions, returned in a Python list, taken from the inputs
	"""
	# identify the smaller of the two dictionaries
	check_dict = None
	if len(dict1) < len(dict2):
		check_dict = dict1
	else: check_dict = dict2
	# find the common elements i.e. a spelling error in both dictdionaries
	my_dict = dict()
	for d1 in dict1:
		if d1 in dict2:
			my_dict[d1] = list(set(dict1[d1] + dict2[d1]))
	return my_dict

def spell_checker_q1_mutiple_languages(dv_list, pwl, text):
	"""
	General
	- this function allows one to use multiple dictionaries and identify errors that don't occur in any of the chosen dictionaries
	- I'm using it because I often muddle UK and US English and
	Inputs
	- dv_list: list of dictionary version inputs e.g. ["en_US", "en_UK"]
	Outputs
	- a Python-dictionary
	- contains spelling errors that occur in all of the chosen dictionaries
	- suggested corrections are taken from each language
	"""

	if len(dv_list) == 1: # if there is only once language selected, proceed as normal
		return spell_checker_q1_single_language(dv_list[0], pwl, text)
	else:
		spelling_errors_multiple_languages_dict = spell_checker_q1_single_language(dv_list[0], pwl, text) # instantiate the return dictionary with the results of the first language dictionary
		for dv in dv_list[1::1]: # iterate over all other dictionaries
			spelling_errors_multiple_languages_dict = intersection_of_two_dicts(spelling_errors_multiple_languages_dict, spell_checker_q1_single_language(dv, pwl, text)) # reduce the return object to the intersection of existing errors and newly found errors
		return spelling_errors_multiple_languages_dict # return the Python-dictionary



def possible_correction_list_to_dict(pcl):
	"""
	General
	- turns a Python-list into a Python-dictionary
	- key: position to be typed into spell check command
	- value: value to change error into
	"""
	pcd = dict()
	index = 0
	for item in pcl:
		pcd[index] = item
		index += 1
	return pcd



def corrections_and_amendments(spelling_errors_multiple_languages_dict, text, pwl):
	"""
	General
	- this function allows a user to correct or otherwise deal with identified spelling errors
	Input
	- spelling_errors_multiple_languages_dict: output of spell_checker_q1_mutiple_languages()
	- text: the text to be evaluated
	- pwl: personal word list
	Output
	- the correted text
	"""
	new_text = text # make a copy of the existing text; we don't want to mutate existing data
	for error in spelling_errors_multiple_languages_dict: # iterate over the identified errors
		possible_corrections = spelling_errors_multiple_languages_dict[error] # create a variable containing the possible corrections fo the error
		possible_corrections.sort() # sort the list
		print("Possible Spelling Error: {}".format(error)) # present the error to the user
		print("Possible Corrections: {}".format(possible_correction_list_to_dict(possible_corrections))) # present solutions to the user
		action = input("Do you want to correct (c), skip (s), save (w), or modify (m) the word? ") # determine what the user wants to do
		if action == "c": # make a change in the document
			index = int(input("Type in the appropriate index: "))
			correction = possible_corrections[index]
			new_text = new_text.replace(error, correction)
		elif action == "s": # do nothing i.e. skip
			pass
		elif action == "w":
			with open(pwl, "a") as destination: # save the error as in the pwl i.e. write
				destination.write(error + "\n")
		elif action == "m": # make a bespoke modification to the text
			new_word = input("Please type in the new word: ")
			new_text = new_text.replace(error, new_word)
			further_action = input("Would you like to save the world to the personal word list? y/n") # see if we should add this to the pwl
			if further_action == "y":
				with open(pwl, "a") as destination:
					destination.write(new_word + "\n")
			else:
				pass
		else:
			print("You may have fucked up, but this is just a tool for me to play with, so figure it out yourself.") # this was just made for me for this assignment, so it's neither user friendly nor robust
		print("")
	return new_text # return the new text




if __name__ == "__main__":

	# inputs
	dv_us = "en_US"
	dv_uk = "en_UK"
	pwl = "q1_spell_checker_personal_dictionary.txt"
	text  = open("q1_a.txt").read()
	dv_list = [dv_us, dv_uk]

	# spell_checker_q1 test
	print("")
	print("Making sure the individual language dictionaries work")
	print("US list")
	print(spell_checker_q1_single_language(dv_us, pwl, text))
	print("UK list")
	print(spell_checker_q1_single_language(dv_uk, pwl, text))

	# spell_checker_q1_mutiple_languages test
	print("")
	print("Making sure the multiple language dictionaries work")
	print(spell_checker_q1_mutiple_languages(dv_list, pwl, text))

	# corrections_and_amendments() test
	print("")
	print("Makign sure the correction function works")
	print(corrections_and_amendments(spell_checker_q1_mutiple_languages(dv_list, pwl, text), text, pwl))


