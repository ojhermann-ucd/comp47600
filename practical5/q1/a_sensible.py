# FUNCTIONS

def jaccard_intersection_magnitude(string_1, string_2):
	# determine the shorter of the two strings
	small, large = None, None
	if len(string_1) < len(string_2):
		small = string_1.split()
		large = string_2.split()
	else:
		small = string_2.split()
		large = string_1.split()
	# determine magnitude of the intersection
	magnitude = 0
	for item in small:
		if item in large:
			magnitude += 1
	# return
	return magnitude

def jaccard_union_magnitude(string_1, string_2):
	return len(string_1) + len(string_2)

def jaccard_index(string_1, string_2):
	return round(float(jaccard_intersection_magnitude(string_1, string_2) / jaccard_union_magnitude(string_1, string_2)), 2)

def jaccard_distance(string_1, string_2):
	return 1 - jaccard_index(string_1, string_2)

print(jaccard_distance("otto was here", "otto is here"))
print(jaccard_distance("otto was here", "otto her here"))