from sqlalchemy import or_
from main import app,db
from .models import *
from .values import *
import hashlib
import os
import ipfsapi


api = ipfsapi.connect('127.0.0.1', 5001)

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
	post_hash = uploadPost(title, text)
	post = Post(post_hash, blog_id)
	db.session.add(post)
	db.session.commit()
	return post.hash
	

def uploadPost(title, text):
	temp_name = title.replace(' ', '-')
	template = open('templates/post.html').read()
	template = template.replace('%TITLE%', title).replace('%TEXT%', text)
	outfile = open('temp_posts/'+temp_name+'.html', 'w+')
	outfile.write(template)
	outfile.close()
	res = api.add('temp_posts/'+temp_name+'.html')
	post_hash = res['Hash']
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
	db.session.commit()


def uploadBlog(name):
	ipns = ''
	return ipns

