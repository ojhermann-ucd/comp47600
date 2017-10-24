# imports
import itertools
import editdistance



# DATA
normal_tweets = [
	"Robert Webb @arobertwebb This was a top chat with an instinctively great interviewer. Big fan of @mrjamesob",
	"J.K. Rowling @jk_rowling Retweeted Lumos @lumos Violence, coercion, abuse of power. Children are trafficked into institutions become vulnerable to modern slavery. #antitraffickingday",
	"Janey Godley Retweeted Angry Scotland @AngryScotland Tory MP will miss a parliamentary vote on universal credit to run the line at a Champions League game instead.",
	"Caroline O. liked Manu Raju @mkraju Conservative blogger Chuck Johnson has been asked to turn over docs to Senate Intel over this but he won't cooperate",
	"Robert Web @arobertwebb Retweeted Marcoooos! @marcusbrig The Young Ones On Comic Relief THIS...sometimes I need this. https://www.youtube.com/watch?v=NhqlrQ64f2Y",
]

spam_list = [
	[0, "Roberto", "Roger"],
	[1, "Webb", "Wes"],
	[2, "@robertowebb", "@rogerailes"],
	[5, "@mugabi", "@marcusaurelius"],
	[16, "https://www.youtube.com/watch?v=ERw-Frq6knI", "https://www.youtube.com/watch?v=dTcvmmOkqJI"],
]

def spam_index(integer):
	length = len(list("{0:b}".format(integer - 1))) # size of containters
	spam_indices = list()
	for k in range(integer):
		binary_elements = list("{0:b}".format(k))
		temp_list = [0 for k in range(length - len(binary_elements))]
		for b in binary_elements:
			temp_list.append(int(b))
		spam_indices.append(temp_list)
	return spam_indices

def make_spam(tweet, spam_index, spam_list):
	tweet_list = tweet.split()
	count = 0
	for index in spam_index:
		spam_change = spam_list[count][index + 1]
		tweet_index = spam_list[count][0]
		tweet_list[tweet_index] = spam_change
		count += 1
	return " ".join(tweet_list)



if __name__ == '__main__':

	my_tweet = normal_tweets[4]
	spam_indices = spam_index(32)
	spam_examples = list()
	for si in spam_indices:
		spam_examples.append(make_spam(my_tweet, si, spam_list))
	normal_examples = normal_tweets[0:4:1]

	print("Normal Tweets Levenshtein Distance from my_tweet")
	count = 0
	normal_average = 0
	for n in normal_examples:
		l_score = editdistance.eval(my_tweet, n)
		print("Normal_{}: {}".format(count, l_score))
		normal_average += l_score
		count += 1
	print("")
	normal_average /= count
	print("Average Levenshtein Score for a Normal Tweet: {}".format(round(normal_average,2)))
	print("")
	print("")

	print("Spam Tweets Levenshtein Distance from my_tweet")
	count = 0
	spam_average = 0
	for s in spam_examples:
		l_score = editdistance.eval(my_tweet, s)
		print("Spam_{}: {}".format(count, l_score))
		spam_average += l_score
		count += 1
	print("")
	spam_average /= count
	print("Average Levenshtein Score for a Spam Tweet: {}".format(round(spam_average,2)))
	print("")
	print("")

	print("Ratio of spam_average to normal_average: {}".format(round(spam_average / normal_average, 2)))
	print("")
	print("The spam tweets distinguish themselves from my tweet by being, on average, having less distance than normal tweets")
	print("This is to be expected as spam tweets, as we were asked to construct them, attempt to mimic normla tweets.")
	print("Similarly, each of the normal tweets is relatively qutie different, especially keeping in mind that twitter has a 140 character limit on tweet sizes")
	print("Similar results obtain for each of the normal tweets, as we'd expect given the spamming strategy we've employed.")
	print("")
	print("")
