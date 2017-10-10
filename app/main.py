#main.py

# [START app]
import logging

# [START imports]
from flask import Flask, render_template, request
# [END imports]

# [START create_app]
app = Flask(__name__)
# [END create_app]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html")
