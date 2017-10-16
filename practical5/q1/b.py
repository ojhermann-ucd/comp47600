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

	