from sqlalchemy import or_
from main import app,db
from .models import *
from .values import *

def isBlog(name, hash):
	blog = Blog.query.filter_by(ipns=hash).first()
	return blog.id if blog else False

def getBlogIPNS(id):
	blog = Blog.get(id)
	return blog.ipns

def newPost(title, text, author, blog_id):
	post_hash = uploadPost()
	blog_ipns = getBlogIPNS(blog_id)
	post = Post(post_hash, blog_id, blog_ipns)


def newBlog(name):
	ipns = uploadBlog(name)
	blog = Blog(ipns)


def uploadBlog(name):
	ipns = ''
	return ipns


def uploadPost():
	post_hash = ''
	return post_hash