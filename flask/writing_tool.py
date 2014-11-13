from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from collections import Counter
import wikipedia
import math
import unicodedata

app = Flask(__name__)

def get_page(t1):
    t1_page = wikipedia.page(t1)
    t1_content = [] 
    t1_content = t1_page.content.split()
    t1_final = []

    x = 0
    while t1_content[x] != '==':
        t1_final.append(unicodedata.normalize('NFKD', t1_content[x]).encode('ascii','ignore')) 
        x+=1

    t1_final = ' '.join(t1_final)
    return t1_final

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

## ROUTING FUNCTIONS
@app.route('/similarity')
def similarity():
    t1 = request.args.get('t1')
    t2 = request.args.get('t2')
    sim = None
    if t1!=None and t2!=None:
      sim = compute_sim(t1, t2)
    if sim==None:
      sim = 0
    return jsonify(result = sim)

@app.route('/fetch')
def fetch():
    t = request.args.get('t')
    text = ""
    if t!=None:
        text = get_page(t)
    return jsonify(result = text)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/', methods=['POST', 'GET'])
def index():
    topic = request.args.get('topic')
    text = None
    if topic:
      text = get_page(topic)

    t1 = request.args.get('t1')
    t2 = request.args.get('t2')
    _sim = None
    if t1!=None and t2!=None:
      _sim = compute_sim(t1, t2)

    return render_template('main.html', topic = text, sim = str(_sim))

if __name__ == "__main__":
    app.run()

