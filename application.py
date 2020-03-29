from flask import Flask
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)

db_host = os.environ['DB_HOST_PROXY']
db_user = os.environ['DB_USER']
db_name = os.environ['DB_NAME']
db_pass = os.environ['DB_PASS']
db_source = db_user + ":" + db_pass + "@tcp(" + db_host + ":3306)/" + db_name

@app.route("/hello")
def hello():
    logger.info(db_host)
    logger.info(db_user)
    logger.info(db_name)
    logger.info(db_pass)
    logger.info(db_source)
    return "Hello"

@app.route("/world")
def world():
    return "World"

