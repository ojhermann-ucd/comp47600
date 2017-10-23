# IMPORTS
import nltk
from nltk.corpus import names
import random


# FUNCTIONS
def gender_features(word):
	return {'last_letter': word[-1]}
# gender_features('Shrek') = {'last_letter': 'k'}

def last_n_letters(word, n):
	if n < len(word):
		return {'last_n_letters': word[-n:]}
	else:
		return {'last_n_letters': word}

def first_n_letters(word, n):
	if n < len(word):
		return {'first_n_letters': word[:-n]}
	else:
		return {'first_n_letters': word}


if __name__ == '__main__':

	# get names
	male_names = [(name, 'male') for name in names.words('male.txt')]
	female_names = [(name, 'female') for name in names.words('female.txt')]
	labeled_names = male_names + female_names
	# shuffle names
	random.shuffle(labeled_names)
	
	# feature_sources
	feature_sources = list()
	for k in range(1, 10, 1):
		feature_sources.append([(last_n_letters(name, k), gender) for (name, gender) in labeled_names])
	# train and test
	number_of_last_letters = 1
	for fs_list in feature_sources:
		training_data = fs_list[int(len(fs_list)/2):]
		testing_data = fs_list[:int(len(fs_list)/2)]
		classifier = nltk.NaiveBayesClassifier.train(training_data)
		print("Accuracy when using the last {} letters: {}".format(number_of_last_letters, nltk.classify.accuracy(classifier, testing_data)))
		classifier.show_most_informative_features(5)
		print("")
		number_of_last_letters += 1

	# feature_sources
	feature_sources = list()
	for k in range(1, 10, 1):
		feature_sources.append([(first_n_letters(name, k), gender) for (name, gender) in labeled_names])
	# train and test
	number_of_last_letters = 1
	for fs_list in feature_sources:
		training_data = fs_list[int(len(fs_list)/2):]
		testing_data = fs_list[:int(len(fs_list)/2)]
		classifier = nltk.NaiveBayesClassifier.train(training_data)
		print("Accuracy when using the first {} letters: {}".format(number_of_last_letters, nltk.classify.accuracy(classifier, testing_data)))
		classifier.show_most_informative_features(5)
		print("")
		number_of_last_letters += 1