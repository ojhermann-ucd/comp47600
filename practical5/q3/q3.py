# imports
import itertools
import editdistance



# DATA
normal_tweet_list = [
	"Dear @POTUS: Based on your weak response to Puerto Rico & remarks about the Virgin Islands' President, I made this cheat sheet to help you.", # https://twitter.com/tedlieu/status/920381148865314816
	"Pigs. In the Pacific.#exploringpigs",	
	"General Kelly, we are so very sorry that @potus has dragged your son’s memory into his web of lies.",
	"i saw a thread about this bizarre racist dingus tweet, then i looked at the replies to the original and it plays so well as a setup and punchline",
	"Anybody that lived for years in a 4 x 4 cage is not intimidated by a loudmouth with a 4-dollar haircut.",
]

spam_elements = [
	"#Kardashians",
	"#SexTape",
	"#XXX",
	"#BonerPills",
	"#Sex",
]

spam_add_ons = ["".join(x) for x in list(itertools.combinations(spam_elements, 2))]

