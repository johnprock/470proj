from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

def compute_sim(t1, t2):
    t1_page = wikipedia.page(t1)
    t2_page = wikipedia.page(t2)

    t1_content = []
    t2_content = []

    t1_content = t1_page.content().split()
    t2_content = t2_page.content().split()
    t1_final = []
    t2_final = []
    x = 0
    while text_box1[x] != '==':
        t1_final.append(text_box1[x]) 
        x+=1

    x = 0
    while text_box2[x] != '==':
        t2_final.append(text_box2[x]) 
        x+=1

    t1_final = str(t1_final)
    t2_final = str(t2_final)
    return 0

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

