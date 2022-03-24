import json
import os
from flask import Flask,request
from src.db.db_utils import DatabaseConnection, TableNames
from src.commons.logging_utils import get_logger


app = Flask(__name__)

logger = get_logger()

@app.route("/health/", methods=["GET", "POST"])
def health():
    return "The show is going well :D"

@app.route('/register', methods=["GET","POST"])
def register():
    
    db_connector = DatabaseConnection()
    try:
        db_connector.add_data_into_table({"username":"venakt","password":"pass"},TableNames.login.value)
    except Exception as e:
        logger.exception(e)    
        return "success"
    return "success"

@app.route('/login', methods=["GET","POST"])
def login():
    # username = request.form.get("username")
    # password = request.form.get("password")
    username = "venakt"
    password = "pass"
    db_connector = DatabaseConnection()
    try:
        result = db_connector.get_result_from_query(f"select * from login where username='{username}'")
        print(result)
        if result and list(result[0])[1]==password:
            return "login success"
        else:
            return "login failed"
    except Exception as e:
        logger.exception(e)    
        return "success"
    return "success"

@app.route('/profile', methods=["GET","POST"])
def profile():
    db_connector = DatabaseConnection()
    try:
        data = {}
        data["username"] = "venakt"
        data["primary_cont"] = "anudeep"
        data["secondary_cont"] = "sushanth"
        
        db_connector.add_data_into_table(data,TableNames.user_details.value)
    except Exception as e:
        logger.exception(e)    
        return "success"
    return "success"

@app.route('/get_data/<username>', methods=["POST"])
def get_user_data(username):
    db_connector = DatabaseConnection()
    try:
        result = db_connector.get_result_from_query(f"select * from user_details where username='{username}'")
        print(result)
    except Exception as e:
        logger.exception(e)
    return "success"

@app.route("/qrcode", methods=["GET"])
def get_qr_code():
    return "qr_code"