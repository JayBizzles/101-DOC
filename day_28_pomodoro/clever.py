# What is the average number of students per section

import requests


url = "https://clever.com/v3.0/courses"

querystring = {"owner_type": "district"}

headers = {
    "Accept": "application/json"
}

response = requests.request("GET", url, headers=headers)

print(response.url)

print(response.links)