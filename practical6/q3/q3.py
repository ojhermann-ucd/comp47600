# SOURCE
# http://pythonprogramming.net/support-vector-machine-svm-example-tutorial-scikit-learn-python/


# IMPORTS
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm


# FUNCTIONS
def get_data():
	return datasets.load_digits()

def get_classifier(free_parameter, cost_function_parameter):
	return svm.SVC(gamma = free_parameter, C = cost_function_parameter)

def get_training_data(digits, number_left_out):
	return [digits.data[:-number_left_out], digits.target[:-number_left_out]]

def get_fitted_svm(free_parameter, cost_function_parameter, digits, number_left_out):
	classifier = get_classifier(free_parameter, cost_function_parameter)
	training_data = get_training_data(digits, number_left_out)
	X, y = training_data[0], training_data[1]
	classifier.fit(X, y)
	return classifier

def get_prediction(classifier, digits, number_left_out):
	return classifier.predict(digits.data[-number_left_out])

def get_visualisation(digits, number_left_out):
	plt.imshow(digits.images[-number_left_out], cmap = plt.cm.gray_r, interpolation = "nearest")
	return plt


if __name__ == '__main__':
	# source data
	digits = get_data()

	# classifier
	classifier = get_fitted_svm(0.01, 100, digits, 1)

	# prediction
	print("Prediction: {}".format(get_prediction(classifier, digits, 1)))

	# visualisation
	this_image = get_visualisation(digits, -1)
	this_image.show()