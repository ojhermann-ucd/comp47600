#Taken from https://datasciencelab.wordpress.com/2013/12/12/clustering-with-k-means-in-python/
# Just added plotting for 3-k cases

import numpy as np
import random
import matplotlib.pyplot as plt

def init_board(N):
	X = np.array([(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(N)])
	return X

def cluster_points(X, mu):
	clusters  = {}
	for x in X:
		bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) for i in enumerate(mu)], key=lambda t:t[1])[0]
		try:
			clusters[bestmukey].append(x)
		except KeyError:
			clusters[bestmukey] = [x]
	return clusters

def reevaluate_centers(mu, clusters):
	newmu = []
	keys = sorted(clusters.keys())
	for k in keys:
		newmu.append(np.mean(clusters[k], axis = 0))
	return newmu

def has_converged(mu, oldmu):
	return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))

def find_centers(X, K):
	# Initialize to K random centers
	oldmu = random.sample(X, K)
	mu = random.sample(X, K)
	while not has_converged(mu, oldmu):
		oldmu = mu
		# Assign all points in X to clusters
		clusters = cluster_points(X, mu)
		# Reevaluate centers
		mu = reevaluate_centers(oldmu, clusters)
	return(mu, clusters)

def change_coords(array):
	return list(map(list, zip(*array)))

def parse_output(data):
	clusters = data[1]
	points1 = change_coords(clusters[0])
	plt.plot(points1[0], points1[1], 'ro')
	points2 = change_coords(clusters[1])
	plt.plot(points2[0], points2[1], 'g^')
	points3 = change_coords(clusters[2])
	plt.plot(points3[0], points3[1], 'ys')
	centroids = change_coords(data[0])
	plt.plot(centroids[0], centroids[1], 'kx')
	plt.axis([-1.0, 1, -1.0, 1])
	plt.show()


if __name__ == '__main__':

	# inputs
	number_of_points = 15
	iterations = 10
	number_of_clusters = 3

	# create the data
	data_runs = list()
	for j in range(iterations):
		data_runs.append(list(init_board(number_of_points)))

	# organise the data
	mu_dict = dict()
	cluster_dict = dict()
	counter = 0
	for run in data_runs:
		center = find_centers(run, number_of_clusters)
		# parse_output(center) # uncomment if you want graphs
		mu_dict[counter] = center[0]
		cluster_dict[counter] = center[1]
		counter += 1

	# count repeats
	mu_set = set()
	cluster_set = set()
	for c in range(counter):
		mu_array = mu_dict[c]
		for pair in mu_array:
			mu_set.add(tuple(pair))
		super_cluster_array = cluster_dict[c]
		for index in super_cluster_array:
			cluster_array = super_cluster_array[index]
			for pair in cluster_array:
				cluster_set.add(tuple(pair))
	print("{} out of {} mu values are unique".format(len(mu_set), len(mu_dict) * number_of_clusters))
	print("{} out of {} cluster values are unique".format(len(cluster_set), len(cluster_dict) * number_of_points))