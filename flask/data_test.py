from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

def compute_sim(t1, t2):
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

