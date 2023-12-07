# the way to import .CSS file or images, javascript through html
# Be sure to create folder and absolute path like example
from flask import Flask, render_template
# import specific blueprint (remember noticed the absolute path)
# the first "second" represent for the file name, 
# the second "second" represent for second.py's blueprint's name
from admin.second import second


app = Flask(__name__)
# register_blueprint so that we can access blueprint's function
# the first parameter represent for specific blueprint's name, 
# the second parameter means that all the routes defined within the second Blueprint will have a URL path that starts with "/admin"
# Ex: reference from second.py, in following case, /admin/home will direct webpage to home.html
app.register_blueprint(second, url_prefix="/admin")

@app.route("/")
def test():
    return "<h1>Test</h1>"

if __name__ == "__main__":
    app.run(debug = True)
