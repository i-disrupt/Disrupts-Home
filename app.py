from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/privacy")
def privacy():
    return render_template('privacy.html')

@app.route("/guidelines")
def guidelines():
    return render_template('guidelines.html')


if __name__ == "__main__":
    app.run()