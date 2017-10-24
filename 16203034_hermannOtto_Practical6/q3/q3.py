# SOURCE
# http://pythonprogramming.net/support-vector-machine-svm-example-tutorial-scikit-learn-python/
# https://www.quora.com/What-are-C-and-gamma-with-regards-to-a-support-vector-machine
# https://www.researchgate.net/post/Does_anyone_know_what_is_the_Gamma_parameter_about_RBF_kernel_function


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

	for d in range(5, 11, 1):
		classifier = get_fitted_svm(0.01, 100, digits, d)
		print("Prediction for {} digits: {}".format(d, get_prediction(classifier, digits, d)))
		this_image = get_visualisation(digits, d)
		this_image.show()
		print("")

	"""
	C
	- higher values make a "hard margin" and allows fewere errors when fitting the model (compared to lower C)
	- higher/"harder" C could lead to overfitting the training data
	- lower/"softer" C could allow for a more generalisable model
	Gamma
	- if too large, then the radius of the area of influence of the area of support vecors only includes the support vector itself and will lead to overfitting
	- if too small, then the model will not be able to capture the complexity of the data; the region of influence of any support vector would be all the training data, so it would behave like a linear model i.e. not capture the non-linear nature and complexity of the data
	"""