from nltk.corpus import wordnet as wn

def synonym(word):
	word = wn.synset('dog.n.01')
	return word.hypernyms()