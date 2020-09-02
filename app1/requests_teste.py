import json

import requests

# get = requests.get('http://127.0.0.1:8000/')

# request_data
# post = requests.post('http://127.0.0.1:8000/request/', data={"person": "Erickson"}).json()

# response_data
post = requests.post('http://127.0.0.1:8000/response/', data={"person": "Erickson"})
print(post.json())
print(post.headers)

