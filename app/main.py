#main.py

# [START app]
import logging

# [START imports]
from flask import Flask, render_template, request
from google.cloud import datastore
from google.auth.exceptions import DefaultCredentialsError
# [END imports]

# [START create_app]
app = Flask(__name__, static_url_path='/static')
# [END create_app]

# [START routing]
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    print(request.form['contactName'])
    print(request.form['contactEmail'])
    print(request.form['contactSubject'])
    print(request.form['contactMessage'])
    # TODO: Implement email
    return "Gotcha"


@app.route('/datastore')
def gcloud():
    # Instantiates a client
    try:
        datastore_client = datastore.Client('python-181206')
    except DefaultCredentialsError:
        return "Run into authentication problem"

    # The kind for the new entity
    kind = 'Task'
    # The name/ID for the new entity
    name = 'sampletask3'
    # The Cloud Datastore key for the new entity
    task_key = datastore_client.key(kind, name)

    # Prepares the new entity
    task = datastore.Entity(key=task_key)
    task['description'] = u"Buy milk"

    # Saves the entity
    datastore_client.put(task)

    return 'Saved {}: {}'.format(task.key.name, task['description'])


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html")
# [END routing]

if __name__ == '__main__':
    app.run()
