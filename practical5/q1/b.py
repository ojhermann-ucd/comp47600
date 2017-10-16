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

	test_string = "12345"
	test_list = list(test_string)
	length_of_test_list = len(test_list)
	jaccard_empirical_list = list()
	for j in range(length_of_test_list):
		for k in range(j+1, length_of_test_list + 1, 1):
			jaccard_empirical_list.append(" ".join(test_list[j:k]))
	jaccard_empirical_list.sort(key = len)
	print("")
	print("Empircal Demonstration of the Triangle Inequality Holding for Jaccard Distance")
	for item in jaccard_empirical_list:
		print("{} = JD({}, {})".format(qs_distance("1 2 3 4 5", item), "1 2 3 4 5", item))