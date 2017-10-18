# imports
import itertools
import editdistance



# DATA
tweet_1 = "Mark Sparrow @Markgsparrow Just a quick reminder that it's almost time to start preparing for those Halloween 'trick or treaters'."

spam_elements_1 = [
	"#JackSparrow",
	"#caribbean",
	"#pirates",
	"#johnny",
	"#depp",
	"https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiyou_Y4_nWAhXIt-0KHcI3CfYYABAAGgJkZw&ohost=www.google.ie&cid=CAESQeD2OwnLHoY9fjS50cd-M3vP0N9jVdSnx1nrM_6BetOc9YbRTTQWgItmbNYK1pepFqI7u390fNxm7ZRcMbHiu-iA&sig=AOD64_1_z5nLfU68bmH0r7WgCCy2wgDUvg&q=&ved=0ahUKEwifverY4_nWAhUFM8AKHT1UCNoQ0QwIJQ&adurl="
]


tweet_2 = "@reginalddhunter Reginald D Hunter Retweeted Mark Sparrow @Markgsparrow Just a quick reminder that it's almost time to start preparing for those Halloween 'trick or treaters'."

spam_elements_2 = [
	"@hunterboots",
	"#boots",
	"#https://www.google.ie/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjYgZH25fnWAhXRFsAKHSu9CH8QFgjAAjAA&url=https%3A%2F%2Fwww.hunterboots.com%2F&usg=AOvVaw0OVbqIevrwiO3h5rbe7q23",
	"#rainyday",
	"@boots",
	"#wet",
]


# DATA FUNCTIONS
def spam_add_ons(spam_elements, additions):
	return ["".join(x) for x in list(itertools.combinations(spam_elements, additions))]

def create_data(tweet, spam_elements, additions):
	output_list = list()
	add_ons = spam_add_ons(spam_elements, additions)
	for i in range(len(add_ons)):
		output_list.append(tweet + add_ons[i])
	return output_list



# GENERATE THE DATA
print("Levenshtein Distance for \"{}\" and Spam Versions".format(tweet_1))
for spam in create_data(tweet_1, spam_elements_1, 2):
	print("Spam Elements: {}".format(spam))
	print(editdistance.eval(tweet_1, spam))
print("")

print("Levenshtein Distance for \"{}\" and Spam Versions".format(tweet_2))
for spam in create_data(tweet_2, spam_elements_2, 2):
	print("Spam Elements: {}".format(spam))
	print(editdistance.eval(tweet_2, spam))
print("")