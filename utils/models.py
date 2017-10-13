from main import app, db

class Blog(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(42))
	ipns = db.Column(db.Text)

	def __init__(self, ipns):
		self.ipns = ipns

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	post_hash = db.Column(db.Text)
	blog_id = db.Column(db.Integer)
	blog_ipns = db.Column(db.Text)

	def __init__(self, post_hash, blog_id, blog_ipns):
		self.hash = post_hash
		self.blog_id = blog_id
		self.blog_ipns = blog_ipns