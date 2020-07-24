# DEPENDENCIAS:
# FLASK
# FLASK_MYSQL
from datetime import date, timedelta

from flask import Flask, render_template, request, redirect, url_for, json, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port=5000, debug=False)