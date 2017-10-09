# imports




def tf_boolean(term_dict, text):
	for word in text:
		if word in term_dict:
			term_dict[word] += 1
	return term_dict



def tf_log_scalred(term_dict, text, base):
	log_dict = tf_boolean(term_dict, text)
	for word in log_dict:
		log_dict[word] = log(log_dict[word], base) + 1
	return log_dict



