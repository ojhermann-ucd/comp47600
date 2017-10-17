# imports
import math
import td_idf


# Documents
document_1 = "I like the talking heads."
document_2 = "I love the talking heads."
document_3 = "I enjoy the talking heads."
document_4 = "I really enjoy the talking heads."
document_list = [document_1, document_2, document_3, document_4]



# TF-IDF functions
term_dict = td_idf.get_terms(document_list)
base = 2
tf_idf_dict = td_idf.tf_idf_boolean(document_list, term_dict, base)

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

for d in document_list:
	print(d, tf_idf_vectors(d, tf_idf_dict))


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

v1 = tf_idf_vectors(document_4, tf_idf_dict)
v2 = tf_idf_vectors(document_1, tf_idf_dict)
print(cosine_similarity(v1, v2))