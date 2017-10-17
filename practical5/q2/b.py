# imports
import math
import td_idf
import a



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

	# Magnitudes
	magnitude_list = [a.magnitude(v) for v in vector_list]

	# Cosine Similarities
	cs_list = [a.cosine_similarity(vector_list[0], v) for v in vector_list]

	# graph data
	graph_data = list()
	for k in range(len(magnitude_list)):
		graph_data.append((magnitude_list[k], cs_list[k]))
	print("List of (magnitude, slope) for the data")
	for k in range(len(magnitude_list)):
		print("Document {}".format(k+1))
		print(graph_data[k])
		print("")
