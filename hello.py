from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1> This is a test"

@app.route("/test")
def test():
    return "test"

if __name__ == "__main__":
    app.run()

