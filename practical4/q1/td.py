# imports




def tf_boolean_dict(term_dict, text):
	"""
	Inputs
	- term_dict: key: item from text, value: instantiated at 0
	- text: string of the text t
	"""
	for item in text:
		if item in term_dict:
			term_dict[item] += 1
	return term_dict

def tf_boolean(term_dict)