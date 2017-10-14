from flask import Flask, render_template, redirect, url_for, request
from werkzeug import secure_filename

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from utils import values

import os

app = Flask(__name__)
app.config.from_pyfile('utils/config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from utils import models, db_handler
db.create_all()


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/newpost/', methods=['POST'])
def newpost():
	form = request.form
	text = form['text']
	title = form['title']
	key = form['key']
	blog_id = db_handler.getBlogByKey(key)
	if blog_id:
		post_hash = db_handler.newPost(title, text, blog_id)
		print(post_hash)
		return redirect('/post/'+post_hash)
	else:
		return 'Bad Key'

@app.route('/post/<post_hash>/')
def post(post_hash):
	return redirect('https://gateway.ipfs.io/ipfs/'+post_hash+'/', code=302)