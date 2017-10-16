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
	wf_1 = "0 0 0"
	wf_2 = "0 0 1"
	wf_3 = "0 1 0"
	wf_4 = "0 1 1"
	wf_5 = "1 0 0"
	wf_6 = "1 0 1"
	wf_7 = "1 1 0"
	wf_8 = "1 1 1"
	wf_list = [wf_1, wf_2, wf_3, wf_4, wf_5, wf_6, wf_7, wf_8]
	

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

	#
	analytic_proof = "https://arxiv.org/pdf/1612.02696.pdf"
	print("")
	print("Analytic Proof of Triangle Inequality Satisfaction: {}".format(analytic_proof))

	# Succint empirical demonstration of the triangle inequality holding for Jaccard measures
	demo_list = [w.split() for w in wf_list]

	print("")
	print("Succint empirical demonstration of the triangle inequality holding for Jaccard Distance")
	for d in demo_list:
		a = d[0]
		b = d[1]
		c = d[2]
		print("a = {}, b = {}, c = {}".format(a, b, c), end = " --> ")
		print("JD(a,c) = {} \u2264 {} = JD(a,b) + JD(b,c) = {} + {}".format(jaccard_distance(a, c), jaccard_distance(a,b) + jaccard_distance(b, c), jaccard_distance(a,b), jaccard_distance(b,c)))
		print("")