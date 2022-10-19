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
	return render_template('login.html', error="User with given username does not exist or password is incorrect")


@app.route('/registration/', methods=['GET'])
def registration_page():
	return render_template('registration.html')


@app.route('/registration/', methods=['POST'])
def registration():
	name = request.form.get('name', '')
	login = request.form.get('login', '')
	password = request.form.get('password', '')

	if not name or not login or not password:
		return render_template('registration.html', error="Please, fill all the inputs")
	cursor.execute('SELECT 1 FROM service.users WHERE login=%s LIMIT 1', (str(login),))
	if cursor.fetchone():
		return render_template('registration.html', error="User with given username already exists")

	cursor.execute(
		'INSERT INTO service.users(full_name, login, password) VALUES (%s, %s, %s)',
		(str(name), str(login), str(password))
	)
	conn.commit()

	return render_template('login.html')
