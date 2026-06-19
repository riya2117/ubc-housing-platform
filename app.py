from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/listings")
def listings():
    return render_template("listings.html")

@app.route("/create-listing")
def create_listing():
    return render_template("create-listing.html")

@app.route("/listing-details")
def listing_details():
    return render_template("listing-details.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True)