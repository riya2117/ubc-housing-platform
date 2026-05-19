from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/listings")
def listings():
    return render_template("listings.html")

@app.route("/create")
def create():
    return render_template("create-listing.html")

if __name__ == "__main__":
    app.run(debug=True)