from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from collections import Counter
from util import *
import util

import math
import unicodedata

app = Flask(__name__)

## ROUTING FUNCTIONS
@app.route('/tool')
def get_tool():
    tool = request.args.get('tool')
    f = tool + ".html"
    return jsonify(result = render_template(f))

@app.route('/merge')
def get_merge():
    text = request.args.get('text')
    s = top_sim_sentences(text)
    return jsonify(s1 = s[0], s2 = s[1])

@app.route('/synonym')
def get_synonym():
    word = request.args.get('word')
    return jsonify(result = synonym(word))

@app.route('/similarity')
def similarity():
    fetch = request.args.get('fetch')
    edit = request.args.get('edit')
    sim = None
    if fetch!=None and edit!=None:
      sim = compute_sim(fetch, edit)
    if sim==None:
      print "sim calculation failed"
      sim = 0
    return jsonify(result = sim)

@app.route('/search')
def search():
    s = request.args.get('text')
    topic = request.args.get('topic')
    print "finding similar"
    f = search_similar(s, topic)
    return jsonify(result = f)

@app.route('/anastrophe')
def anastrophe():
   sentence = request.args.get('s')
   print "anastrophizing"
   ana = util.anastrophe(sentence)
   print "returning " + ana
   return jsonify(result = ana) 

@app.route('/fetch')
def fetch():
    t = request.args.get('t')
    text = ""
    if t!=None:
      text = get_page(t)
    print "returning"
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

