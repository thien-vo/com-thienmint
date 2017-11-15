from google.cloud import datastore
from google.auth.exceptions import DefaultCredentialsError
import logging, traceback

import google.auth
# [Create credentials and project name]
credentials, project = google.auth.default()


def get_info():
    try:
        datastore_client = datastore.Client(
            project=project,
            credentials=credentials
        )
        kind = 'com-thienmint'
        name = 'zoho_config'
        task_key = datastore_client.key(kind, name)

        email_entity = datastore_client.get(task_key)
        return email_entity['username'], email_entity['password']
    except DefaultCredentialsError:
        print("Run into authentication problem")
        return None, None
    except Exception as e:
        logging.error(traceback.format_exc())
        return None, None

if __name__=='__main__':
    print "Find email/password configuration in Datastore"
