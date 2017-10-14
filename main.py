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
		return redirect('/post/'+post_hash)
	else:
		return render_template('index.html', text=text, title=title, bad_key=True)

@app.route('/newblog/', methods=['GET', 'POST'])
def newblog():
	if request.method=='POST':
		form = request.form
		blog_name = form['name']
		author_name = form['author']

		error = db_handler.validate_sumbission(blog_name, author_name)
		if error:
			return render_template('new_blog.html', error=error)

		key = db_handler.newblog(blog_name)
		return render_template('new_blog.html', key=key)
	
	else:
		return render_template('new_blog.html')


@app.route('/post/<post_hash>/')
def post(post_hash):
	return redirect('https://gateway.ipfs.io/ipfs/'+post_hash+'/', code=302)

@app.route('/checkBlogName/<blog_name>/')
def checkBlogName(blog_name):
	return str(db_handler.blogExists(blog_name))


@app.route('/checkAuthor/<author>/')
def checkBlogName(author):
	return str(db_handler.authorExists(author))
