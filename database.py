from GAPP import db, User, Post

db.create_all()     # create tables from models

user1 = User(
    username='Manidills'
)

post1 = Post()
post1.title = "IRON_MAN is alive"
post1.body = "We love IRON_MAN 3000"
post1.author = user1

db.session.add(post1)
db.session.add(user1)
db.session.commit()

print(User.query.all())
print(Post.query.all())
