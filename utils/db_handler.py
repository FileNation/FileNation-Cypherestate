from sqlalchemy import or_
from main import app,db
from .models import *
from .values import *
import hashlib
import os
import ipfsapi


api = ipfsapi.connect('127.0.0.1', 5001)

def getBlogByKey(key):
	key = getSHA(key.encode('utf-8'))
	blog = Blog.query.filter_by(key=key).first()
	return blog.id if blog else False


def newPost(title, text, blog_id):
	template = fillPostTemplate(title, text)
	post_file = createPostFile(title, template)
	post_hash = uploadPost(post_file)
	addPostToDB(post_hash, blog_id)
	return post_hash
	
	
def fillPostTemplate(title, text):
	template = open(post_template).read()
	template = template.replace('%TITLE%', title).replace('%TEXT%', text)
	return template


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


def addPostToDB(post_hash, blog_id):
	post = Post(post_hash, blog_id)
	db.session.add(post)
	db.session.commit()


def newBlog(author, name):
	template = fillBlogTemplate(author, name)
	blog_file = createBlogFile(name, template)
	ipns = uploadBlog(blog_file)
	key = generateBlogKey() 
	addBlogToDB(ipns, key, author)
	return key


def fillBlogTemplate(author, name):
	template = open(blog_template).read()
	template = template.replace('%AUTHOR%', author).replace('%NAME%', name)
	return template


def createBlogFile(name, template):
	temp_name = name.replace(' ','-')
	outfile = open(temp_blogs+temp_name+'.html', 'w+')
	outfile.write(template)
	outfile.close()
	return temp_name

def uploadBlog(blog_file):
	pass
	return ipns


def generateBlogKey():
	key = generateKey()
	if keyExists(key):
		generateBlogKey()
	return key


def addBlogToDB(ipns, key, name, author):
	blog = Blog(ipns, key, author)
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
	blog_key = getSHA(blog_key)
	Blog.query.filter_by(key=blog_hash)


def isBlog(name, hash):
	blog = Blog.query.filter_by(ipns=hash).first()
	return True if blog else False


def validateSubmission(blog_name, author_name):
	if db_handler.blogExists(blog_name):
		return 'blog_exists'	
	if db_handler.authorExists(author_name):
		return 'author_exists'
	return False
