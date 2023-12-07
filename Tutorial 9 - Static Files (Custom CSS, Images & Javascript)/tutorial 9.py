# the way to import .CSS file or images, javascript through html
# Be sure to create folder and absolute path like example
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True)
