from main import app, db


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(42))
    ipns = db.Column(db.Text)
    key = db.Column(db.Text)
    author = db.Column(db.String(42))
    hash = db.Column(db.Text)

    def __init__(self, blog_hash, key, name, author):
        self.key = key
        self.name = name.replace(' ', '-')
        self.author = author.replace(' ','-')
        self.hash = blog_hash


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_hash = db.Column(db.Text)
    blog_id = db.Column(db.Integer)
    title = db.Column(db.Text)

    def __init__(self, post_hash, blog_id, title):
        self.post_hash = post_hash
        self.blog_id = blog_id
        self.title = title
