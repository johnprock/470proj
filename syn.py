from nltk.corpus import wordnet as wn

def synonym(word):
	word_list = wn.synsets(word)
	syns = []
	size = len(word_list)
	x = 0
	while x < size:
		syn = word_list[x]
		syn = str(syn)
		syn = syn.split('.')[0]
		syn = syn.split("'",1)[-1]
		syns.append(syn)
		x += 1
	synonyms = set(syns)
	synonyms = list(synonyms)
	print synonyms
