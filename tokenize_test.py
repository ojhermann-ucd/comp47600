import nltk

rawtext = open("tokenise_test.txt", "r").read()

tokens = nltk.word_tokenize(rawtext)
print(tokens)