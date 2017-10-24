# IMPORT

import csv
import random
import math
import operator
from collections import defaultdict # brining in to make things faster for Q1
import plotly.plotly as py
import plotly.graph_objs as go
import random


# FUNCTIONS
def get_source_data(file_name):
	with open(file_name, 'r') as csv_file:
		data_list = list(csv.reader(csv_file))
		for sub_list in data_list:
			for j in range(len(sub_list) - 1):
				sub_list[j] = float(sub_list[j])
	return data_list

def get_data_for_k_folding(data_list, k):
	# data
	if len(data_list) < k: # if k is too large, we cannot proceed
		return False
	random.shuffle(data_list) # shuffle the data; we could stratify the data if required
	k_data_lists = [[] for j in range(k)] # return object: list of k lists filled with source data
	# populate k_data_lists
	k_index = 0
	for j in range(len(data_list)): # iterate over each entry in data_list
		k_data_lists[k_index].append(data_list[j]) # add the data
		k_index += 1
		if k_index == k:
			k_index = 0
	# return
	return k_data_lists

def generate_test_training_pairs(k_data_lists):
	k = len(k_data_lists)
	test_training_pairs = list()
	for j in range(k):
		test_set = k_data_lists[j]
		training_set = list()
		for h in range(k):
			if h != j:
				training_set += k_data_lists[h]
		test_training_pairs.append([test_set, training_set])
	return test_training_pairs


def euclidean_distance(instance_1, instance_2, length):
	distance = 0
	for j in range(length - 1):
		distance += math.pow(instance_1[j] - instance_2[j], 2)
	return math.sqrt(distance)

def get_k_neighbours(training_list, test_instance, k):
	length = len(test_instance)
	distances = [(training_instance ,euclidean_distance(training_instance, test_instance, length)) for training_instance in training_list]
	distances.sort(key=operator.itemgetter(1))
	# return neighbours
	return [distances[j][0] for j in range(k)]

def get_response(neighbours):
	class_votes = dict()
	for n in neighbours:
		if n[-1] in class_votes:
			class_votes[n[-1]] += 1
		else:
			class_votes[n[-1]] = 1
	sorted_votes = sorted(class_votes.items(), key=operator.itemgetter(1), reverse=True)
	return sorted_votes[0][0]

def get_predictions(training_list, test_list, k):
	predictions = list()
	for test_instance in test_list:
		neighbours = get_k_neighbours(training_list, test_instance, k)
		predictions.append(get_response(neighbours))
	return predictions

def get_accuracy(test_list, predictions):
	correct = 0
	length = len(test_list)
	for j in range(length):
		if test_list[j][-1] == predictions[j]:
			correct += 1
	return float(correct / length) * 100



if __name__ == '__main__':

	# inputs
	file_name = "iris.csv"
	k = 5

	# generate data
	data_list = get_source_data(file_name)
	k_data_lists = get_data_for_k_folding(data_list, k)
	test_training_pairs = generate_test_training_pairs(k_data_lists)

	# analysis
	average_accuracy = 0
	for pair in test_training_pairs:
		test_list = pair[0]
		training_list = pair[1]
		predictions = get_predictions(training_list, test_list, k)
		accuracy = get_accuracy(test_list, predictions)
		average_accuracy += accuracy
	average_accuracy /= k
	print("{}-Average Accuracy: {}".format(k, average_accuracy))