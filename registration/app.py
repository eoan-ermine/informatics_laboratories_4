from os import getenv

import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

import psycopg2
import psycopg2.extras


load_dotenv()


app = Flask(__name__)
conn = psycopg2.connect(
	database=getenv("PG_DATABASE"), user=getenv("PG_USER"), password=getenv("PG_PASSWORD"),
	host=getenv("PG_HOST"), port=getenv("PG_PORT")
)
cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


@app.route('/login/', methods=['GET'])
def index():
	return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login():
	username = request.form.get('username', '')
	password = request.form.get('password', '')

	if not username or not password:
		return render_template('login.html', error="Please, fill all the inputs")

	cursor.execute('SELECT * FROM service.users WHERE login=%s AND password=%s', (str(username), str(password)))
	record = cursor.fetchone()

	if record:
		return render_template('account.html', **record)
	return render_template('login.html', error="User with given username does not exist")
