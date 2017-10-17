# imports
import math
import td_idf
import a
import b
from scipy import spatial
"""
https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.distance.euclidean.html
https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.distance.cosine.html
"""



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
	vector_list = [a.tf_idf_vectors(d, tf_idf_dict) for d in document_list]
	scipy_vectors = list()
	for v in vector_list:
		temp_list = list()
		for key in v:
			temp_list.append(v[key])
		scipy_vectors.append(temp_list)

	# scipy_evaluation
	count = 0
	for sv in scipy_vectors:
		print("Original: {}".format(document_list[count]))
		print("Vector: {}".format(sv))
		print("Cosine Similarity: {}".format(round(1 - spatial.distance.cosine(scipy_vectors[0], sv),2)))
		print("Cosine Distance: {}".format(round(spatial.distance.cosine(scipy_vectors[0], sv),2)))
		print("Euclidean Distance: {}".format(round(spatial.distance.euclidean(scipy_vectors[0], sv),2)))
		print("")
		count += 1