from main import app, db

class Blog(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(42))
	ipns = db.Column(db.Text)
	key = db.Column(db.Text)
	author = db.Column(db.String(42))
	hash = db.Column(db.Text)

	def __init__(self, ipns, blog_hash, key, name, author):
		self.ipns = ipns
		self.key = key
		self.name = name
		self.author = author
		self.hash = blog_hash

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	post_hash = db.Column(db.Text)
	blog_id = db.Column(db.Integer)

	def __init__(self, post_hash, blog_id):
		self.hash = post_hash
		self.blog_id = blog_id