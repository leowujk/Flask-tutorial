# Sessions
# it's temporary, simple, and stored on the web server 
# for quick access of information between all the differents pages
# Ex: skip login pages to already-login state, if I already login before
from flask import Flask, redirect, url_for, render_template, request, session
# to set up the max time that session could last
from datetime import timedelta
app = Flask(__name__)
# secret_key is neccessary for encrypt and decrypt session's data message
app.secret_key = "hello"
# Permanent session - define how long I want a permanent session to last
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        # define following session as a permanent session
        session.permanent = True 
        # session is like a dictionary which can stores data
        session["user"] = user
        return redirect(url_for("user"))
    else:
        # if you have been login, you can skip to the user pages
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")
@app.route("/user")
def user():
    # if user access user() from login() function
    # it's a way to post information in the session
    # below's "user" means session's own key
    if "user" in session:
        # user is the another variable from login()
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        # or else, redirect it to the origin url + /login
        return redirect(url_for("login")) #don't plus slash in front of the login 

@app.route("/logout")
def logout():
    # remove user data from the session
    # If the first argument is not found as a key, it will return the second argument.
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)