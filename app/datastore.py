# Imports the Google Cloud client library
from google.cloud import datastore
from google.auth.exceptions import DefaultCredentialsError

# Instantiates a client
try:
    datastore_client = datastore.Client(
        project='python-181206',
    )

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

    print('Saved {}: {}'.format(task.key.name, task['description']))
except DefaultCredentialsError:
    print("Caught Error")
