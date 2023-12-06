# Using SQLAlchemy Database
# store specific information (like email) to the database
# Ex: When log in, save already-typed information in specific blank and show off
# you have to install first : pip install flask-sqlalchemy, and import it
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)
# sets the URI (Uniform Resource Identifier) for the database that SQLAlchemy will use.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
# Setting it to False turns off the modification tracking.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# put this project into database
db = SQLAlchemy(app)
# create a Model
class users(db.Model):
    # first parameter is column's name, second one is variable's type, third one is for primary key or foreign key 
    # name used in the code represents the name of the column in the database table. 
    # It is not the variable's name in the Python code; 
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    # This allows you to set the initial values for the name and email attributes when creating a new user object.
    # The __init__ method is called automatically when you create a new instance of the class.
    def __init__(self, name, email):
    # Don't need to add _id, cuz database can auto-incrementing primary keys.
        self.name = name
        self.email = email
    # Without the __init__ method, you would need to set the values of name and email after creating the object:
    
    
    # Ex 1:
    # user_instance = users()
    # user_instance.name = "John Doe"
    # user_instance.email = "john@example.com"
    
    
    # Ex 2:
    # Manually specifying the primary key
    # new_user_with_id = users(_id=123, name="Jane Doe", email="jane@example.com")



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session.permanent = True 
        session["user"] = user
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
        # Code for handling the case when the user is logging in for the first time
        if request.method == "POST":
            # got input "email" from user.html in <form> </form>
            email = request.form["email"]
            # grab that information to the session's variable
            session["email"] = email
            flash("Email was saved!")
        # Code for handling the case when it's not a POST request (user is not logging in for the first time)
        # will access the blocks'stored information instead of submitting
        else:
            if "email" in session:
                email = session["email"]
        # show off the already-filled information in the user.html's input value blank
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
    # clear the "email" part in the session
    session.pop("email", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)