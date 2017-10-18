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

focus_tweet = normal_tweets[4].split()
# ['Robert', 'Web', '@arobertwebb', 'Retweeted', 'Marcoooos!', '@marcusbrig', 'The', 'Young', 'Ones', 'On', 'Comic', 'Relief', 'THIS...sometimes', 'I', 'need', 'this.', 'https://www.youtube.com/watch?v=NhqlrQ64f2Y']
first_name_dict = {"Roberto":0, "Roger":0}
second_name_dict = {"Webb":1, "Wes":1}
at_dict_1 = {"@robertowebb":2, "@rogerailes":2}
at_dict_2 = {"@mugabi":5, "@marcusaurelius":5}
url_dict = {"https://www.youtube.com/watch?v=ERw-Frq6knI":16, "https://www.youtube.com/watch?v=dTcvmmOkqJI":16}





# DATA FUNCTIONS
def spam_add_ons(spam_elements, additions):
	return ["".join(x) for x in list(itertools.combinations(spam_elements, additions))]

def create_data(tweet, spam_elements, additions):
	output_list = list()
	add_ons = spam_add_ons(spam_elements, additions)
	for i in range(len(add_ons)):
		output_list.append(tweet + add_ons[i])
	return output_list