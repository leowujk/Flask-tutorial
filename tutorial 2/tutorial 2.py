# don't add any "specific symbols" comments in the html file, or it will went wrong
# render_template allows you to import html, javascipts, css
from flask import Flask, redirect, url_for, render_template
# create a folder names "templates" (name is unchangeable) and create html file in it
app = Flask(__name__)

# the page will be not found, you must add a parameter behind original url so that it will show something
@app.route("/<name>")
def home(name):
    #don't add anything comments line in html, or it will report error
    return render_template("index.html", content=["Allen","Jeff","Jecica"])

# for easier to demo
if __name__ == "__main__":
    app.run()   