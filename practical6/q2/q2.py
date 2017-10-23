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

	"""
	I extended the given formul to allow for n last letters and compared it to one allowing for n first letters
	I also modified the code to use all of the data: 50% in training and 50% in test
	- this could easily be modified to change either the split or volume of total data used
	I've included a graph of one run of the two metrics
	- note that given I shuffle the data, each run will be slightly different
	- however, all runs demonstrate the same behaviour
	In this data set, using 2 of the last letters is the most accurate predictor, both on an accuracy score of 77% and on finding the highest average odds of individual names e.g. 'na' is 93.5:1 a female name
	It would be interesting to run this type of analysis, but to stratify the names by geography, culture, or other metrics e.g. I would expect Latin American names with generised suffixes to be highly predictive of gender, but the phenomena would not be predictive with Germanic names
	"""