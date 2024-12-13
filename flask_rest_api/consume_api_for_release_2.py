"""
1. Getting All Records
2. Adding New Records
"""

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
    print("Please check whether my_rest_api_release_2.py is running")
    exit()

print("#"*40, end="\n\n")
#############################

print("POST: Adding New Record")
print("-"*20)
# -----------

try:
    import requests
    api_response = requests.post("http://127.0.0.1:5000/postdbdata",
                                 json={"IP":'123.123.123.126', "DATE":'12/Dec/2024',"PICS":'abc.jpg', "URL":"www.abcxyz.com"}
                                 )
    api_data = api_response.json()
    print(api_data)
except Exception as e:
    print("Error Occurred while accessing API and details:", e, sep="\n\n", end="\n\n")
    print("Please check whether my_rest_api_release_2.py is running")
    exit()

print("#"*40, end="\n\n")
#############################
