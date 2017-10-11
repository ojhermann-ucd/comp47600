# imports
import glob
import q1



if __name__ == "__main__":
	
	# go to the files
	q1.go_a_to_tweets()
	
	# iterate over all the files
	print("")
	print("TF Boolean Scores")
	for file_name in glob.glob("*.tweet"):
		# tf_boolean
		tf_boolean = q1.tf_boolean(file_name)
		print("File Name: {} TF Boolean Scores".format(file_name))
		print(tf_boolean)
		print("")

	#
	print(q1.get_file_names())
	print(q1.get_terms())