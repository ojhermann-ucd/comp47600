# imports
import math
import td_idf



# TF-IDF functions
def tf_idf_vectors(document, tf_idf_dict):
	vector = dict() # instantiate the vector
	for term in tf_idf_dict:
		if document in tf_idf_dict[term]:
			if term in vector:
				vector[term] += tf_idf_dict[term][document]
			else:
				vector[term] = tf_idf_dict[term][document]
		else:
			vector[term] = 0
	return vector


# COSINE SIMILARITY
def dot_product(A, B):
	dp = 0
	for key in A:
		dp += A[key] * B[key]
	return dp

def magnitude(A):
	sum_of_A = 0
	for key in A:
		sum_of_A += A[key]**2
	return math.sqrt(sum_of_A)

def cosine_similarity(V1, V2):
	numerator = dot_product(V1, V2)
	denominator = magnitude(V1) * magnitude(V2)
	return round(float(numerator / denominator), 2)



if __name__ == '__main__':

	# Documents
	document_1 = "I like the talking heads."
	document_2 = "I love the talking heads."
	document_3 = "I enjoy the talking heads."
	document_4 = "I really like the talking heads."
	document_5 = "I really enjoy the talking heads."
	document_6 = "I really love the talking heads."
	document_list = [document_1, document_2, document_3, document_4, document_5, document_6]

	# Term Dictionary
	term_dict = td_idf.get_terms(document_list)
	base = 2

	# TF-IDF Dictionary
	tf_idf_dict = td_idf.tf_idf_boolean(document_list, term_dict, base)

	# Vectors
	vector_list = [tf_idf_vectors(d, tf_idf_dict) for d in document_list]

	# Cosine Similarities
	count = 0
	for v in vector_list:
		print("Original: {}".format(document_list[count]))
		print("Vector: {}".format(v))
		print("Cosine Similarity: {}".format(cosine_similarity(vector_list[0], v)))
		print("")
		print("")
		count += 1