# IMPORTS



# FUNCTIONS
def jaccard_index(string_1, string_2):
	# modify the input strings
	set_1 = set(string_1.split())
	set_2 = set(string_2.split())

	# set operations
	intersection = set_1.intersection(set_2)
	union = set_1.union(set_2)

	# jaccard values
	intersection_count = len(intersection)
	union_count = len(union)

	# jaccard_index
	jaccard_index_value = float(intersection_count / union_count)
	
	# return
	return round(jaccard_index_value, 2)


def jaccard_distance(string_1, string_2):
	return round(float(1 - jaccard_index(string_1, string_2)), 2)


def pairs_in_a_list_matrix(a_list, metric):
	# list of tuples
	list_of_lists = list()

	# number of items in a_list
	number_of_items = len(a_list)

	# iteratively obtain the pairs
	for j in range(number_of_items - 1): # only want up to the penultimate item in the list
		row_list = ["-" for x in range(number_of_items)] # create an empty list
		for k in range(j+1, number_of_items):
			a_pair = [a_list[j], a_list[k]] # create a tuple of j-indexed-item and all other items not paired with it already
			if metric == "jd":
				row_list[k] = jaccard_distance(a_pair[0], a_pair[1])
			else:
				row_list[k] = jaccard_index(a_pair[0], a_pair[1])
		list_of_lists.append(row_list)

	# return
	return list_of_lists


def pairs_in_a_list_matrix_with_labels(a_list, metric):
	# create the core of the matrix
	matrix = pairs_in_a_list_matrix(a_list, metric)

	# labels_list
	labels_list = list()
	if metric == "jd":
		labels_list.append("Jaccard Distance")
	else:
		labels_list.append("Jaccard Index")
	count = 1
	for item in a_list: # iteratively add the titles of the word features
		labels_list.append("wf_{}".format(count))
		count += 1

	# print
	print(" ".join(["{:>16}".format(item) for item in labels_list])) # print column labels
	count = 1
	for row in matrix:
		temp_row = row
		temp_row.insert(0, labels_list[count])
		print(" ".join(["{:>16}".format(item) for item in temp_row]))
		count += 1







if __name__ == '__main__':


	# word features
	wf_1 = "My favourite band is the Talking Heads".lower()
	wf_2 = "My favourite musicians are the Talking Heads".lower()
	wf_3 = "I like the Talking Heads".lower()
	wf_4 = "I don't like television featuring talking heads".lower()
	wf_5 = "Many racists favour the opinions of talking heads on Fox News".lower()
	wf_6 = "I like the phrase talking heads".lower()
	wf_list = [wf_1, wf_2, wf_3, wf_4, wf_5, wf_6]
	

	# Word Features
	print("Word Features")
	count = 1
	for wf in wf_list:
		print("wf_{}: {}".format(count, wf))
		count += 1

	# Jaccard Distance
	print("")
	pairs_in_a_list_matrix_with_labels(wf_list, "jd")
	
	# Jaccard Index
	print("")
	pairs_in_a_list_matrix_with_labels(wf_list, "ji")

	# Empirical demonstration of the triangle inequality holding for Jaccard measures
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
		print("{} = JD({}, {})".format(jaccard_distance("1 2 3 4 5", item), "1 2 3 4 5", item))
	print("")
	print("Empircal Demonstration of the Triangle Inequality Holding for Jaccard Indexing")
	for item in jaccard_empirical_list:
		print("{} = JD({}, {})".format(jaccard_index("1 2 3 4 5", item), "1 2 3 4 5", item))

	# write up outline
	analytic_proof = "https://arxiv.org/pdf/1612.02696.pdf"
	print("")
	print("Analytic Proof of Triangle Inequality Satisfcation by Jaccard Distance: {}".format(analytic_proof))