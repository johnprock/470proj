from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from collections import Counter
from util import *

import math
import unicodedata

app = Flask(__name__)

## ROUTING FUNCTIONS
@app.route('/tool')
def get_tool():
    tool = request.args.get('tool')
    f = tool + ".html"
    return jsonify(result = render_template(f))

@app.route('/synonym')
def get_synonym():
    word = str(request.args.get('word'))
    print word
    print "generating synonym"
    print synonym(word)
    print "synonym success"
    return jsonify(result = synonym(word))

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

