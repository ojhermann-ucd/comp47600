# imports
import os
import glob
import nltk
from nltk.corpus import stopwords
import math



# DIRECTORY CHANGES
def go_q2_to_tweets():
	os.chdir("Tweets_no_stop")

def go_tweets_to_q2():
	os.chdir("../")



# FILE NAMES
def get_file_names():
	# file_name_list
	file_name_list = list()
	for file_name in glob.glob("*tweet"):
		file_name_list.append(file_name)
	return file_name_list



# FILE TO LIST
def file_to_list(file_name):
	with open(file_name, "r") as source:
		return source.read().split()



# LIST TO NGRAM LIST
def ngram_end(file_list, n):
	if len(file_list) < n:
		return len(file_list) - 1
	else:
		return len(file_list) - n + 1

def list_to_ngram_list(file_list, n):
	ngram_list = list()
	if len(file_list) < n:
		return [" ".join(file_list)]
	else:
		for i in range(0, ngram_end(file_list, n), 1):
			ngram_list.append(file_list[i:i+n])
	return ngram_list






if __name__ == '__main__':

	go_q2_to_tweets()
	file_name_list = get_file_names()
	for file_name in file_name_list:
		file_contents_list = file_to_list(file_name)
		file_ngrams = list_to_ngram_list(file_contents_list, 2)
		print(file_contents_list)
		print(file_ngrams)
		print("")