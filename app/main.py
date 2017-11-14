#main.py

# [START app]
import logging

# [START imports]
from flask import Flask, render_template, request
# [END imports]

# [START create_app]
app = Flask(__name__, static_url_path='/static')
# [END create_app]

# [START routing]
@app.route('/')
def home():
    return render_template("home.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html")
# [END routing]

if __name__ == '__main__':
    app.run()
