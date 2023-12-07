# In Flask, a Blueprint is a way to organize a group of related views, templates, and static files.
# It allows you to modularize your application by breaking it into smaller, reusable components. 
# Each Blueprint can have its own set of routes, templates, and static files.
from flask import Blueprint, render_template
# first and second parameter means "creates a blueprint named second", 'static_folder' and 'template_folder' all reference to existed folder name
second = Blueprint("second", __name__ , static_folder = "static", template_folder="templates") 


# define a route within the Blueprint named "second" and it's function
@second.route("/home")
def home():
    # print(2)
    return render_template("home.html")