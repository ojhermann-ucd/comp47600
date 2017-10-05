# imports




# input variables
wc_input = "May our children and our children's children to a thousand generations, continue to enjoy the benefits conferred upon us by a united country, and have cause yet to rejoice under those glorious institutions bequeathed us by Washington and his compeers."
wc_output = "children washington thousand enjoy glorious country united compeers may childrens upon benefits bequeathed yet cause conferred rejoice continue generations institutions"



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