# HTTP Methods (GET/POST) & Retrieving Form Data
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
# route should be accessible for both HTTP POST and GET methods.
# POST method : "submitting" the "form"
# GET method : "loading" the "specific page"
@app.route("/login", methods=["POST", "GET"])
# the function's name doesn't determine to the url
def login():
    if request.method == "POST":
        user = request.form["nm"]
        # if press submit button, it will redirect to the "user" webpage, and show what you got
        return redirect(url_for("user",usr=user))
        # if you don't post anything, it will hang in login.html
        # you must notice that not just .html file, .py file's function can also show the webpage
        # despite it doesn't have it's own html file.
    else:
        # below is the "GET" method
        return render_template("login.html")
# "/<usr>" is a parameter which can take any value, which is differnt from "/usr", has specific route
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)