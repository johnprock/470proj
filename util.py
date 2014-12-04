from collections import Counter
import math


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

    terms = set(c1).union(c2)
    dot_product = sum(c1.get(x, 0) * c2.get(x, 0) for x in terms)
    magnitude1 = math.sqrt(sum(c1.get(x,0)**2 for x in terms))
    magnitude2 = math.sqrt(sum(c2.get(x,0)**2 for x in terms))
    mag_product = magnitude1*magnitude2
    if mag_product == 0:
        return 0 
    return dot_product/mag_product








