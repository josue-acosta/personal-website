# import 'from'
from flask import Flask, render_template


# app config
app = Flask(__name__, static_url_path='/static')


# GET /
@app.route("/")
def home():
    return render_template("home.html"), 200


# GET /about
@app.route('/about')
def about():
    return render_template("about.html"), 200


# GET /projects
@app.route('/projects')
def projects():
    return render_template("projects.html"), 200


# GET /contact
@app.route('/contact')
def contact():
    return render_template("contact.html"), 200


# GET /coming-soon
@app.route('/coming-soon')
def coming_soon():
    return render_template("other/coming_soon.html"), 200


# GET /404
@app.errorhandler(404)
def page_not_found(error):
    return render_template("other/404.html"), 404



## Run App Config
if __name__ == '__main__':
    app.run(debug=True)