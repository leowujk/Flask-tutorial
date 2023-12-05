from flask import Flask, redirect, url_for

app = Flask(__name__)

# if you want to find home page, always start from root
@app.route('/')
# something to show (page)
def home():
    return "Hello! this is the main page <h1>HELLO</h1>"
@app.route("/<name>")
# if someone visits "/John", the user("John") function will be called, 
# and it will return the string "Hello John!".
def user(name):
    return f"Hello {name} !"
# add "/admin" on the original url
# if use /admin, on the url, "/admin/" or "/admin" is ok
@app.route("/admin/")
def admin():
    # back to the "user" page, and "user" page's parameter is Allen
    return redirect(url_for("user", name="Allen"))

# for easier to demo
if __name__ == "__main__":
    app.run()   
