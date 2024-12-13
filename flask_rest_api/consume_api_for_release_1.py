"""
Requests Library for Accessing APIs
"""

print("Accessing Weather API")
print("-"*20)
# -----------

import requests
api_response = requests.get("https://demoqa.com/utilities/weather/city/pune")
api_data = api_response.json()
print(api_data)
print(type(api_data))

print("#"*40, end="\n\n")
#############################

print("GET: Getting all records")
print("-"*20)
# -----------

try:
    import requests
    api_response = requests.get("http://127.0.0.1:5000/getdbdata")
    api_data = api_response.json()
    print(api_data)
except Exception as e:
    print("Error Occurred while accessing API and details:", e, sep="\n\n", end="\n\n")
    print("Please check whether my_rest_api_release_1.py is running")
    exit()

print("#"*40, end="\n\n")
#############################
