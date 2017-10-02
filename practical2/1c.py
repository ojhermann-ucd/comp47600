# imports




# input variables
wc_input = "This is my text.  It contains about thirty words, of which I expect roughly half to be excluded as stop words.  If I modified the input of the R command, I could change the results."
wc_output = "input results half thirty expect change this words stop command contains text excluded modified roughly"



def quote_to_words(string_input):
	letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
	string_output = ""
	for character in string_input:
		if character not in letters:
			pass
		else:
			string_output += character
	return string_output.lower()



def question_results(string_input, string_output):
	input_list = list(set(string_input.split()))
	output_list = list(set(string_output.split()))
	removed_list = [x for x in input_list if x not in output_list]
	return [removed_list, output_list]



wc_input_mod = quote_to_words(wc_input)
results = question_results(wc_input_mod, wc_output)
excluded_list = results[0]
included_list = results[1]
excluded_list.sort()
included_list.sort()


print("original")
print(wc_input)
print("")

print("excluded_list")
print(excluded_list)
print("")

print("included_list")
print(included_list)
print("")


print("excluded_list len")
print(len(excluded_list))
print("")

print("included_list len")
print(len(included_list))
print("")

print("original len")
print(len(set(wc_input_mod.split())))