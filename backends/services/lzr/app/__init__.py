from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="supersupermarket"
    )
    return conn

from app import routes