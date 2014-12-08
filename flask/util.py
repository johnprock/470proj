import wikipedia
from collections import Counter
import math
import unicodedata
import random
import nltk

from nltk.corpus import wordnet as wn # add this thing to requirements file...
from nltk import pos_tag, word_tokenize

def disambiguate(topic):
    try:
        page = wikipedia.page(topic)
    except wikipedia.exceptions.DisambiguationError as e:
        page = wikipedia.page(e.options[0])

    return page
        

def get_page(t1):
    t1_page = disambiguate(t1)
    t1_content = [] 
    t1_content = t1_page.content.split()
    t1_final = []

    x = 0
    while t1_content[x] != '==':
        t1_final.append(unicodedata.normalize('NFKD', t1_content[x]).encode('ascii','ignore')) 
        x+=1

    t1_final = ' '.join(t1_final)
    return t1_final

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
	return synonyms

def top_sim_sentences(paragraph):
	sentences = paragraph.split('.')
	sentences.remove(sentences[-1])
	score = 0
	max_score = 0
	s1 = 0
	s2 = 0
	size = len(sentences)

	y = 1
	x = 0
	while x < size:
		while y < size:
			score = compute_sim(sentences[x], sentences[y])
			if score > max_score:
				max_score = score
				s1 = x
				s2 = y
			y +=1	
		x += 1
		y = x +1

	top_two = []
	top_two.append(sentences[s1])
	top_two.append(sentences[s2])
	return top_two

def compute_sim(t1, t2): #takes two bodies of strings

    c1 = Counter(t1.split())
    c2 = Counter(t2.split())

    terms = set(c1)
    dot_product = sum(c1.get(x, 0) * c2.get(x, 0) for x in terms)
    magnitude1 = math.sqrt(sum(c1.get(x,0)**2 for x in terms))
    magnitude2 = math.sqrt(sum(c2.get(x,0)**2 for x in terms))
    mag_product = magnitude1*magnitude2
    if mag_product == 0:
        return 0 
    return dot_product/mag_product


def replace(text, old_word, new_word):
	
	tokens = []
	tokens = text.split(' ')

	x = 0
	size = len(tokens)
	while x < size:
		if(old == tokens[x]):
			tokens[x] = new
		x += 1

	text = ' '.join(tokens)
	return text

def related_links(topic):
	topic = disambiguate(topic)
	text_box1 = []
	text_box1 = topic.content.split()
	size = len(text_box1)
	related = []
	x = 0

	while x < size:
		if text_box1[x] == "also" and text_box1[x+1] == "==":
			x = x +2
			j = x
			while j < size:
				if text_box1[j] == "==":
					break
				related.append(text_box1[j])
				j += 1
		x += 1

	if not related:
		print 'none'
		return 
	size = len(related)
	x = 0
	while x < size:
		print related[x]
		x += 1
	return

def search_similar(sentence, topic):
    links = disambiguate(topic).links
    top = [] 
    rlinks = []

    
    for i in range(0,10):
        r = random.randint(0, len(links)-1)
        rlinks.append(links[r])

    for link in rlinks:
        print "going to link: " + link
        related_page = disambiguate(link)
        related_sentences = related_page.content.split(".") 
        related_sentences.remove(related_sentences[-1])
         
        sims = [(compute_sim(sentence, rs), rs) for rs in related_sentences]
        sort = sorted(sims, key=lambda tup: tup[0], reverse=True)
        top.append(sort[0])

    return sorted(top, key=lambda tup: tup[0], reverse=True)[0]
        

def anastrophe(sentence):
 
        text = word_tokenize(sentence)
        tup = nltk.pos_tag(text)
        print tup
#        text = sentence
#        tup = [("This", "DT"), ("is", "VB"), ("a", "DT"), ("test", "NN")] #fury the dog was
 
        words = []
        parts = []
        anastrophe = []
        size = len(tup)
        x = 0
        while x < size:
                words.append(tup[x][0])
                x += 1
        x = 0
        while x < size:
                parts.append(tup[x][1])
                x +=1
 
 
        x = 0
        while x < size:
                if parts[x][:2] == "VB":
                        j = x +1
                        while j < size:
                                anastrophe.append(words[j])
                                j+=1
                       
                x += 1
 
        x = 0
        size = len(anastrophe)
        while x < size:
                words.remove(anastrophe[x])
                x += 1
 
 
        x = 0
        size = len(words)
        while x < size:
                anastrophe.append(words[x])
                x +=1
 
        final_anastrophe = ' '.join(anastrophe)
        return final_anastrophe 
