"""
Python for web development
"""

"""
We have many web frameworks in python
flask # Small framework
django # MVT (Model View Template)
many more
"""

"""
We will be using flask framework
"""

"""
Using flask framework
1. Using flask framework we can develop websites
2. Using flask framework we can develop REST-API
3. Using flask framework we can develop MicroServices
"""

"""
We will discuss on 

How to use flask framework for developing REST-API
"""

"""
Example: Suppose we want to provide access to our database with others/public
then how to provide access to our database with others/public?

OPTION-1: We can create separate credentials like username, password and
share. BUT it is LIMITED. Widely means to-public, it is difficult to manage
"""

"""
We have/got 2 solutions
1. SOAP: Simple Object Access Protocol
2. REST: REpresentational State Transfer

both are called architectures/desings/styles
both tells how to provide access

both tells INTRODUCE one INTERFACE/DOOR/GATE between our-app with others
it is like
our-db/our-app <--INTERFACE--> others/public

This INTERFACE is also called as APPLICATION PROGRAMMING INTERFACE(API)

both tells how to write such INTERFACE

SOAP-API
REST-API
"""

"""
REST architecture came after SOAP architecture
- REST is easy to implement/manage
- REST is popular
"""

"""
flask is already implemented REST architecture
- We JUST need to know how to create REST-API using flask
"""

"""
We need web server to run our web-application/API
- flask has builtin web server
- This builtin web server, we can make use for development purpose
    NOT for production
"""

"""
If time permits, We are planning provide FULL-ACCESS/COMPLETE-ACCESS

FULL-ACCESS/COMPLETE-ACCESS means
- Creating new record in db table
- Reading existing records from our db table
- Updating existing records in our db table
- Deleting existing records from our db table
"""

"""
HTTP Standards: Using HTTP Methods

FULL-ACCESS/COMPLETE-ACCESS means
POST        - Creating new record in db table
GET         - Reading existing records from our db table
PUT/PATCH   - Updating existing records in our db table
DELETE      - Deleting existing records from our db table
"""

"""
In this release, we are planning to create
REST-API to provide access to - Reading existing records from our db table

PLANNED REST-API ENDPOINT: http://127.0.0.1:5000/getdbdata
"""

# --------
# Create App
##########
import flask
# my_rest_api_app = flask.Flask("Provide Some Name to Our App")
my_rest_api_app = flask.Flask(__name__) # __name__ having file name
######################


# --------
# END POINT - 1: URL http://127.0.0.1:5000/getdbdata mapped to route("/getdbdata")
##########
@my_rest_api_app.route("/getdbdata", methods=["GET"])
def get_db_data_function():
    """
    Get data from database and return in json
    """
    import sqlite3
    my_db_connection = sqlite3.connect("my_database.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_db_cursor.execute("SELECT * FROM MY_TABLE")
    my_db_result = my_db_cursor.fetchall()
    return flask.jsonify(my_db_result)
######################


# --------
# Run builtin server
##########
my_rest_api_app.run() # default IP=127.0.0.1 PORT=5000
# my_rest_api_app.run(host='', port='')
######################
