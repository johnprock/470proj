from flask import Flask
from flask import render_template
from flask import request
from collections import Counter
import wikipedia
import math

app = Flask(__name__)

def get_page(t1):
    t1_page = wikipedia.page(t1)
    t1_content = [] 
    t1_content = t1_page.content.split()
    t1_final = []

    x = 0
    while t1_content[x] != '==':
        t1_final.append(t1_content[x]) 
        x+=1

    return str(t1_final)

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

@app.route("/")
def data_test():
    return render_template('data_test.html')

@app.route("/sim_score.html")
def sim_score():
    t1 = request.args.get('t1')
    t2 = request.args.get('t2')

    sim = compute_sim(t1, t2)

    return render_template('sim_score.html', sim=str(sim))

if __name__ == "__main__":
    app.run()

