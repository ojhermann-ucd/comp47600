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
	wf_list = list()
	# for i in range(7, 17):
	# 	wf_list.append(" ".join(list("{0:b}".format(i))))
	# wf_list = ["a", "b", "c", "a b", "b c", "a c"]
	wf_list = ["the talking heads are my favourite band", "the talking heads are my favourite musical group", "i enjoy listening to the talking heads", "i hate talking heads on fox news", "fox news is a gaggle of iditotic talking heads", "talking heads annoy me a great deal"]

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
	print("")
	print("Empirical demonstration of the triangle inequality holding for Jaccard Distance")
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
				jd_ac = jaccard_distance(a, c)
				jd_ab = jaccard_distance(a, b)
				jd_bc = jaccard_distance(b, c)
				example_count += 1
				if jd_ac > (jd_ab + jd_bc): # if ac > ab + bc, then the triangle inequality has failed
					incorrect_count += 1
					print("error")
	print("Triangle Inequality obtains for {}/{} checks i.e. all permutations of the word features".format(example_count - incorrect_count, example_count))
	print("")

	print("note that you can extend the list of phrases arebitratily, but eventually you will encounter a combinatorial explosion")