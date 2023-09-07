# from sqlalchemy import or_
#
from sqlalchemy import or_

from module_5.ORM.lesson_10.engine_ import session, User, Post, Comment

# select
# user = session.query(User).filter(or_(User.id == 2 , User.id == 1)).all()
# print(user)


# insert
# post1 = Post(title = "post2" , description = "lorem asdfa fewr ewf sdfgret")
# post2 = Post(title = "post3" , description = "lorem asdfa fewr ewf sdfgret")
#
# session.add_all([post1 , post2])
# session.commit()

# delete
# post = session.query(Post).all()[0]
# print(post)

# session.delete(post)
# session.commit()
# session.query(Post).where(or_(Post.id == 1 , Post.id == 2 , Post.id == 3)).delete()
# session.commit()


# update

# post = session.query(Post).all()[0]
# post.title = "Hello"
# session.commit()

# session.query(Post).where(Post.id == 5).update({"title": "Hello3" , "description" : "lorem afsdgsdafe dfew"})
# session.commit()


# post = session.query(Post).where(Post.id == 5).one()
# print(post.comments)

# com = session.query(Comment).where(Comment.id == 3).one()
# print(com.post.comments)




