import sqlite3
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def get_user():
    name = request.args.get("name")
    conn = sqlite3.connect("test.db")
    # Injection SQL : entrée utilisateur concaténée dans la requête
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return str(conn.execute(query).fetchall())

@app.route("/ping")
def ping():
    host = request.args.get("host")
    # Injection de commande : entrée utilisateur passée au shell
    return subprocess.check_output("ping -c 1 " + host, shell=True)
