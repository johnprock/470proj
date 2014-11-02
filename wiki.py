import wikipedia 

shark = wikipedia.page("Shark")
whale = wikipedia.page("Whale")

text_box1 = []
text_box2 = []
text_box1 = shark.content.split()
text_box2 = whale.content.split()

x = 0
while text_box1[x] != '==':
	print text_box1[x], 
	x+=1

print 
print 
print 


x = 0
while text_box2[x] != '==':
	print text_box2[x], 
	x+=1

