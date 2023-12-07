# PLEASE DO NOT ADD SPECIFIC CHARACTER TO THE HTML.FILE !!!!!
# Learning database's operation
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    # view all querys (we should login first so that there will a message stores in database)
    # "values" represent specific each row (query)
    # "users" means database's table's name, "query" means each row
    return render_template("view.html",values = users.query.all())

@app.route("/login", methods=["POST", "GET"])
def login():
    # user first log in to the page
    if request.method == "POST":
        user = request.form["nm"]
        session.permanent = True 
        session["user"] = user
        # grab specific user row
        # "user" is message we typed, and "query" means database's specific row, and "first" means that we only need one name
        # filter_by function can grab specific row I wanted
        # parameter: "name" means database's specific attribute, "user" means above session resource 
        found_user = users.query.filter_by(name = user).first()
        # if specific user's information is already stored in the database
        if found_user:
            # then grab that specific row's email information to the session so that it will be used someday 
            session["email"] = found_user.email
        # don't find specific user's information in the database
        else:
            usr = users(user, None)
            # and add database to the session
            db.session.add(usr)
            # commit session's each changes
            db.session.commit()
        
        
        # if you want to delete message, just type line like below: change last one into delete()
        # found_user = users.query.filter_by(name = user).delete()
        
        # if you want to delete multiple of them:
        # for user in found_user.email
        #       user.delete()
        
        # and remember commit your modification
        # db.session.commit()

        flash("Login succesful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in")
            return redirect(url_for("user"))
        return render_template("login.html")
@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            # put email into database's specific user row
            found_user = users.query.filter_by(name = user).first()
            # add specific user's email to it's own row
            found_user.email = email
            # commit session's each change
            db.session.commit()
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email = email)
    else:
        flash("You are not logged in !")
        return redirect(url_for("login")) 

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out.","info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
