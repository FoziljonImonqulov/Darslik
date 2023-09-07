from Telegram_bot.ORM.lesson10.engine_ import session,User

a = session.query(User).all()
print(session.query(User).filter(User.id == 2, User.age <= 20).all())

# psot2 = Post(title="post1", description='salom hammaga janoblar')
# session.add(psot2)
# session.commit()

# session.query(Post).where(Post.id == 1).delete()
# session.commit()

# session.query(Post).where(Post.id == 3).update({"title": "Hello", 'description': 'lorem sadfasfkjfkbfbbajbdjabd'})
#
# session.commit()
