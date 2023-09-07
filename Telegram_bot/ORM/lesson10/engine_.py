# pip install SQLAlchemy
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Text
# database://username:password@host/dbname
from sqlalchemy.orm import declarative_base, relationship, mapped_column, Mapped, Session, sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:1@localhost/postgres")
# engine = create_engine("sqlite://///home/userfoziljon/PycharmProjects/Darslik/Telegram_bot/ORM/lesson10/engine_.py")
# engine.connect()

Session = sessionmaker(engine)
session = Session()

Base = declarative_base()


# class User(Base):
#     __tablename__ = "users"
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     fullname: Mapped[str] = mapped_column(__type_pos=String(255), nullable=True)
#     age: Mapped[int] = mapped_column()
#
#     def __repr__(self):
#         return f"id = {self.id}, fullname = {self.fullname}, age = {self.age}"
#
#
# class Post(Base):
#     __tablename__ = 'posts'
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     title: Mapped[str] = mapped_column(__type_pos=String(255))
#     description: Mapped[str] = mapped_column()
#     comments: Mapped[list['Comment']] = relationship(back_populates='post')
#
#
# class Comment(Base):
#     __tablename__ = 'comments'
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     message: Mapped[str] = mapped_column()
#     post: Mapped['Post'] = relationship(back_populates='comments')

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    orders = relationship("Order", back_populates="customer")


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship("Customer", back_populates="orders")


Base.metadata.create_all(engine)
