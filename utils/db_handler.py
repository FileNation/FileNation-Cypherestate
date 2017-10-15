from sqlalchemy import or_
from main import app,db
from .models import *
from .values import *
import hashlib
import os
import ipfsapi
from flask import render_template_string


api = ipfsapi.connect('127.0.0.1', 5001)


def getBlogByKey(key):
	key = getSHA(key.encode('utf-8'))
	blog = Blog.query.filter_by(key=key).first()
	return blog.id if blog else False


def newPost(title, text, blog_id):
	template = fillPostTemplate(title, text)
	post_file = createPostFile(title, template)
	post_hash = uploadPost(post_file)
	post = addPostToDB(post_hash, blog_id, title)
	blog = Blog.query.get(blog_id)
	addPostToBlog(post, blog)
	return post_hash
	
	
def fillPostTemplate(title, text):
	template = open(post_template).read()
	filled = render_template_string(template, title=title, text=text)
	return filled


def createPostFile(title, template):
	temp_name = title.replace(' ', '-')
	outfile = open(temp+temp_name+'.html', 'w+')
	outfile.write(template)
	outfile.close()
	return temp_name


def uploadPost(post_file):
	res = api.add(temp+post_file+'.html')
	post_hash = res['Hash']
	return post_hash


def addPostToDB(post_hash, blog_id, title):
	post = Post(post_hash, blog_id, title)
	db.session.add(post)
	db.session.commit()
	return post


def newBlog(author, name):
	template = fillBlogTemplate(author, name)
	blog_file = createBlogFile(name, template)
	blog_hash = uploadBlog(blog_file)
	key = generateBlogKey() 
	hashed_key = getSHA(key)
	addBlogToDB(blog_hash, hashed_key, name, author)
	return key

def addPostToBlog(post, blog):
	template = fillBlogPosts(blog)
	file = createBlogFile(blog.name, template)
	blog_hash = uploadBlog(file)
	blog.hash = blog_hash
	db.session.commit()

def fillBlogPosts(blog):
	posts = Post.query.filter_by(blog_id=blog.id)
	template = open(blog_template).read()
	filled = render_template_string(
		 template,
		 blog = blog,
		 posts = posts
	)
	return filled

def fillBlogTemplate(author, name):
	template = open(blog_template).read()
	filled = render_template_string(
		template,
	 	title = title, 
	 	author = author
	 )
	return filled


def createBlogFile(name, template):
	temp_name = name.replace(' ','-')
	outfile = open(temp_blogs+temp_name+'.html', 'w+')
	outfile.write(template)
	outfile.close()
	return temp_name

def uploadBlog(blog_file):
	res = api.add(temp_blogs+blog_file+'.html')
	ipfs_path = '/ipfs/'+res['Hash']
	published_data = api.name_publish(ipfs_path, resolve=True, lifetime='175200h')
	return (res['Hash'], published_data['Name'])


def generateBlogKey():
	key = generateKey()
	if keyExists(key):
		generateBlogKey()
	return key


def addBlogToDB(blog_hash, key, name, author):
	blog = Blog(blog_hash, key, name, author)
	db.session.add(blog)
	db.session.commit()


def generateKey():
	rand = os.urandom(24)
	return getSHA(rand)


def getSHA(data):
	return hashlib.sha256(data).hexdigest()

def getBlogIPNS(id):
	blog = Blog.get(id)
	return blog.ipns


def blogExists(name):
	blog = Blog.query.filter_by(name=name).first()
	return True if blog else False


def authorExists(author):
	blog = Blog.query.filter_by(author=author).first()
	return True if blog else False


def keyExists(blog_key):
	blog_key = getSHA(blog_key.encode('utf-8'))
	blog = Blog.query.filter_by(key=blog_key).first()
	return True if blog else False


def isBlog(name, hash):
	blog = Blog.query.filter_by(ipns=hash).first()
	return True if blog else False


def validateSubmission(blog_name, author_name):
	if blogExists(blog_name):
		return 'blog_exists'	
	if authorExists(author_name):
		return 'author_exists'
	return False
