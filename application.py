from flask import Flask
import os
import logging
from infra.mysql import MySQL

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)

db_host = os.environ['DB_HOST_PROXY']
db_user = os.environ['DB_USER']
db_name = os.environ['DB_NAME']
db_pass = os.environ['DB_PASS']
dns = {
    'user': db_user,
    'host': db_host,
    'password': db_pass,
    'database': db_name
}
db = MySQL(**dns)


@app.route("/hello")
def hello():
    stmt = 'SELECT * FROM test WHERE id = ?'
    record = db.query(stmt, '1', prepared=True)
    logger.info(record)

    return "Hello"


@app.route("/world")
def world():
    return "World"

