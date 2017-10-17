# IMPORTS



# FUNCTIONS
def qs(string_1, string_2):
	# modify the input strings
	set_1 = set(string_1.split())
	set_2 = set(string_2.split())

	# numerator
	intersection = set_1.intersection(set_2)
	magnitude_of_intersection = len(intersection)
	numerator = 2 * magnitude_of_intersection

	# denominator
	magnitude_of_set_1 = len(set_1)
	magnitude_of_set_2 = len(set_2)
	denominator = magnitude_of_set_1 + magnitude_of_set_2

	# qs_value
	qs_value = float(numerator / denominator)
	
	# return
	return round(qs_value, 2)


def qs_distance(string_1, string_2):
	return round(float(1 - qs(string_1, string_2)), 2)


if __name__ == '__main__':

		# word features
	wf_list = list()
	# for i in range(7, 17):
	# 	wf_list.append(" ".join(list("{0:b}".format(i))))
	wf_list = ["a", "b", "c", "a b", "b c", "a c"]

	# Word Features
	print("Word Features")
	count = 1
	for wf in wf_list:
		print("wf_{}: {}".format(count, wf))
		count += 1

	# Empirical demonstration of the triangle inequality failing for the Dice Coefficient
	print("")
	print("Empirical demonstration of the triangle inequality failing for the Dice Coefficient")
	example_count = 0 # keep track of examples generated
	incorrect_count = 0 # keep track of number triangle inequality failures
	for first_item in wf_list: # use each item in wf_list
		second_item_list = [w for w in wf_list]
		second_item_list.remove(first_item)
		for second_item in second_item_list: # use every other item in wf_list less the first_item
			third_item_list = [s for s in second_item_list]
			third_item_list.remove(second_item)
			for third_item in third_item_list: # use every other item in wf_list less first_item, second_item
				a = first_item
				b = second_item
				c = third_item
				jd_ac = qs_distance(a, c)
				jd_ab = qs_distance(a, b)
				jd_bc = qs_distance(b, c)
				example_count += 1
				if jd_ac > (jd_ab + jd_bc): # if ac > ab + bc, then the triangle inequality has failed
					incorrect_count += 1
					print("Failure {}: QS(\"{}\",\"{}\") = {} > {} = {} + {} = QS(\"{}\",\"{}\") + QS(\"{}\",\"{}\")".format(incorrect_count, a, c, jd_ac, round(jd_ab + jd_bc,2), jd_ab, jd_bc, a,b,b,c))
	print("")
	fail_percent = round(incorrect_count / example_count, 2)
	print("Triangle Inequality obtains for {}/{} checks i.e. {} of the word feature permutations failed to satisfy triangle inequality".format(example_count - incorrect_count, example_count, fail_percent))
	print("")

	print("Note: you can extend the list of phrases arbitrarily, but eventually you will encounter a combinatorial explosion when tyring to exhaustively enumerate all possible conditions")