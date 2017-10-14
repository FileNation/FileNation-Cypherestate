from sqlalchemy import or_
from main import app,db
from .models import *
from .values import *
import hashlib
import os

def generateKey():
	rand = os.urandom(24)
	return getSHA(rand)

def getSHA(data):
	return hashlib.sha256(data).hexdigest()

def isBlog(name, hash):
	blog = Blog.query.filter_by(ipns=hash).first()
	return blog.id if blog else False

def getBlogByKey(key):
	key = getSHA(key.encode('utf-8'))
	blog = Blog.query.filter_by(key=key).first()
	return blog.id if blog else False

def getBlogIPNS(id):
	blog = Blog.get(id)
	return blog.ipns

def newPost(title, text, blog_id):
	post_hash = uploadPost()
	post = Post(post_hash, blog_id)
	db.session.add(post)
	db.commit()
	return post.hash
	

def uploadPost():
	post_hash = ''
	return post_hash


def keyExists(blog_key):
	blog_key = getSHA(blog_key)
	Blog.query.filter_by(key=blog_hash)


def generateBlogKey():
	key = generateKey()
	if keyExists(key):
		generateBlogKey()
	return key

def newBlog(name):
	ipns = uploadBlog(name)
	key = generateBlogKey() 
	blog = Blog(ipns, key)
	db.session.add(blog)
	db.commit()


def uploadBlog(name):
	ipns = ''
	return ipns

