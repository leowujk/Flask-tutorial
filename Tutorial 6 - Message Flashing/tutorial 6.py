# Message flashing
# When there is something happened on previous GUI, show the previous pages message on the current message
# Ex: When log in, show (flash) the "log in successfully" message on the next pages's top bar 
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session.permanent = True 
        session["user"] = user
        # flash message
        flash("Login succesful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            # flash message
            flash("Already logged in")
            return redirect(url_for("user"))
        return render_template("login.html")
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        # flash message and direct it to user.html 
        return render_template("user.html",user = user)
    else:
        # flash message
        flash("You are not logged in !")
        return redirect(url_for("login")) 

@app.route("/logout")
def logout():
    # when you already log in so that it will show flash message below when you log out
    if "user" in session:
        user = session["user"]
        # show (flash) specific message on the top bar : "You have been logged out !"
        # the second parameter is icon or subcontent
        flash(f"You have been logged out.","info")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)