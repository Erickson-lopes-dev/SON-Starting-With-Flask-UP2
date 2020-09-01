import json

import requests

# get = requests.get('http://127.0.0.1:8000/')

post = requests.post('http://127.0.0.1:8000/request/', data={"person": "Erickson"}).json()

print(post)

