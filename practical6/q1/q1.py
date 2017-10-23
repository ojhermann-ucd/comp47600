# Example of kNN implemented from Scratch in Python
# By Jason Brownlee
# http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

import csv
import random
import math
import operator
from collections import defaultdict # brining in to make things faster for Q1
import plotly.plotly as py
import plotly.graph_objs as go


def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])


def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
def main():
	# prepare data
	trainingSet=[]
	testSet=[]
	split = 0.9
	loadDataset('iris.csv', split, trainingSet, testSet)
	print('Train set: ' + repr(len(trainingSet)))
	print('Test set: ' + repr(len(testSet)))
	# generate predictions
	predictions=[]
	k = 2
	for x in range(len(testSet)):
		neighbors = getNeighbors(trainingSet, testSet[x], k)
		result = getResponse(neighbors)
		predictions.append(result)
		print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
	accuracy = getAccuracy(testSet, predictions)
	print('Accuracy: ' + repr(accuracy) + '%')

def main_modified(split, k):
	# prepare data
	trainingSet=[]
	testSet=[]
	loadDataset('iris.csv', split, trainingSet, testSet)
	while len(trainingSet) < k:
		loadDataset('iris.csv', split, trainingSet, testSet) # added to repeat until appropriate size is achieved
	# generate predictions
	predictions=[]
	if len(trainingSet) < k:
		print("len(trainingSet) < k when split = {} and k = {}".format(split, k)) # check and notification
	else:
		for x in range(len(testSet)):
			neighbors = getNeighbors(trainingSet, testSet[x], k)
			result = getResponse(neighbors)
			predictions.append(result)
		accuracy = getAccuracy(testSet, predictions)
		# return
		return [split, k, accuracy]

def loadDataset_k_folding_naive(filename, k):
	with open(filename, 'r') as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		for x in range(len(dataset)-1):
			for y in range(4):
				dataset[x][y] = float(dataset[x][y])
				# folding happens here
				k_data_sets = [[] for x in range(k)]
				k_index = 0
				for j in range(len(dataset)):
					k_data_sets[k_index].append(dataset[j])
					k_index += 1
					if k_index == k:
						k_index = 0
		# return
		return k_data_sets

def generate_test_training_pairs(k_data_sets):
	k = len(k_data_sets)
	test_training_pairs = list()
	for j in range(k):
		test_set = k_data_sets[j]
		training_set = list()
		for h in range(k):
			if h != j:
				training_set += k_data_sets[h]
		test_training_pairs.append([test_set, training_set])
	return test_training_pairs

def main_modified_k_folding(filename, k):
	# prepare data
	k_data_sets = loadDataset_k_folding_naive(filename, k)
	test_training_pairs = generate_test_training_pairs(k_data_sets)
	# generate predictions
	output = list()
	for pair in test_training_pairs:
		predictions=[]
		neighbors = getNeighbors(pair[1], pair[0], k)
		result = getResponse(neighbors)
		predictions.append(result)
		accuracy = getAccuracy(testSet, predictions)
		output.append(accuracy)
	return output



if __name__ == '__main__':

	# PRINT TOGGLE
	print_status = False

	# results_container
	results_container = defaultdict(dict)

	# SYSTEMATICALLY VARY THE SIZE OF SPLIT AND K
	print("SYSTEMATICALLY VARY THE SIZE OF SPLIT AND K")
	for k in range(1, 21, 1):
		for split in range(1, 91, 1):
			try:
				if print_status:
					result = main_modified(float(split/100), k)
					print("Split: {}".format(result[0]))
					print("k: {}".format(result[1]))
					print("Accuracy: {}".format(result[2]))
					print("")
				else:
					result = main_modified(float(split/100), k)
					results_container[result[1]][result[0]] = result[2]
			except:
				print(split, k, "failure")
	print("")
	"""
	If len(trainingSet) < k, the code will not run
	- line 38 --> line 32 --> line 18 --> line 17
	- tries to find k neighbours but there aren't that many in distances b/c there aren't that many in trainingSet
	- solution: recalculate trainingSet in a while loop until it's large enough and then move on.
	"""

	# PLOT ACCURACY FOR CHANGES
	k_list = [1, 5, 10, 15, 20]
	for k in k_list:
		k_data = results_container[k]
		the_x = [strip for strip in k_data]
		the_y = [k_data[strip] for strip in k_data]
		print("k = {}".format(k))
		print(the_x)
		print(the_y)
		print("")

	# K FOLDING ALGORITHM
	"""
	Generating the k data sets for a k-folded elemnt is straightforward enough.
	Conceptually, implementing the test on this data is also straightforward: for each of the k data sets created, run the k-nearest neighbour algorithm with that data set as test and the others combined as training; take the resulting accuracy scores, sum them, and divide by k to get the average accuracy
	However, to implement it would require modifying each of the underlying functions, which would not be a good use of time for the purposes of this module and the other work I need to complete to demonstrate a grasp of the underyling concepts of text analytics.
	"""
	k_data_sets = loadDataset_k_folding_naive("iris.csv", 5)
	print(len(k_data_sets))
	# main_modified_k_folding("iris.csv", 5), this does not work without modifying all the functions given, but doing to is not a good use of time.