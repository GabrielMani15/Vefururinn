from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    litliReikningurinn = (2 + 2) * 2
    return "<h1>Einn góð stafsetingavilla á þessu haha. upsii!</h1>"

if __name__ == "__main__":
    app.run(debug=True)