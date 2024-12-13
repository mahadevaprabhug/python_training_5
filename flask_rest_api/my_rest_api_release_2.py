"""
Supported

1. End User Can Get all records
    END POINT: http://127.0.0.1:5000/getdbdata

2. End User Can Add new records to our database
    END POINT: http://127.0.0.1:5000/postdbdata
"""

# --------
# Create App
##########
import flask
my_rest_api_app = flask.Flask(__name__)
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
# END POINT - 2: URL http://127.0.0.1:5000/postdbdata mapped to route("/postdbdata")
##########
@my_rest_api_app.route("/postdbdata", methods=["POST"])
def post_db_data_function():
    """
    Our Plan:
    Task-1: Get new record sent by end user({"IP":'123.12.3.1', "DATE":'',"PICS":'', "URL":""})
    Task-2: Check whether IP is already present in our db
    Task-3: Add new record to our database
    """

    # -----------
    # Task-1: Get new record sent by end user({"IP":'123.12.3.1', "DATE":'',"PICS":'', "URL":""})
    # -----------
    received_record = flask.request.get_json()
    # ip = received_record["IP"]
    # OR
    ip = received_record.get("IP")
    dt = received_record.get("DATE")
    img = received_record.get("PICS")
    url = received_record.get("URL")
    ##############

    # -----------
    # Task-2: Check whether IP is already present in our db
    # -----------
    import sqlite3
    my_db_connection = sqlite3.connect("my_database.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_query = f"SELECT * FROM MY_TABLE WHERE IP = '{ip}'"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchone()
    if my_db_result is None:
        my_query = f"INSERT INTO MY_TABLE VALUES ('{ip}', '{dt}', '{img}', '{url}')"
        my_db_cursor.execute(my_query)
        my_db_connection.commit()
        my_db_connection.close()
        return flask.jsonify("New Record Added. Please check DB")
    else:
        return flask.jsonify("Record Already Present")
    ##############

######################

# --------
# Run builtin server
##########
my_rest_api_app.run() # default IP=127.0.0.1 PORT=5000
# my_rest_api_app.run(host='', port='')
######################
