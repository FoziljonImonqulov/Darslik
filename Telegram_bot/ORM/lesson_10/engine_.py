# pip install SQLAlchemy
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship, mapped_column, Mapped, sessionmaker
# database://username:password@host/dbname
engine = create_engine("postgresql+psycopg2://postgres:1@localhost/postgres")
# engine = create_engine("sqlite:////home/dilshod/PycharmProjects/p14_group/module_5/ORM/lesson_10/test.sqlite")
# engine.connect()
# session
Session = sessionmaker(engine)
session = Session()

Base = declarative_base()

# class User(Base):
#     __tablename__ = "users"
#
#     id: Mapped[int] = mapped_column(primary_key=True , autoincrement=True)
#     fullname: Mapped[str] = mapped_column(__type_pos=String(255), nullable=True)
#     age: Mapped[int] = mapped_column()
#
#     def __repr__(self):
#         return f"id = {self.id}| fullname = {self.fullname}| age = {self.age}"
#
# class Post(Base):
#     __tablename__ = 'posts'
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     title: Mapped[str] = mapped_column(__type_pos=String(255))
#     description: Mapped[str] = mapped_column()
#     comments : Mapped[list['Comment']] = relationship(back_populates='post')
#
#     def __repr__(self):
#         return f"{self.__dict__}"
#
# class Comment(Base):
#     __tablename__ = 'comments'
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     post_id : Mapped[int] = mapped_column(ForeignKey("posts.id"))
#     user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
#     message: Mapped[str] = mapped_column()
#     post : Mapped['Post'] = relationship(back_populates='comments')
#
#     def __repr__(self):
#         return f"{self.message}"

# association_table = Table(
#     "association_table",
#     Base.metadata,
#     Column("left_id", ForeignKey("left_table.id")),
#     Column("right_id", ForeignKey("right_table.id")),
# )

class parent_child(Base):
    __tablename__ = "left_table_right_table"
    left_id: Mapped[int] = mapped_column(ForeignKey("left_table.id"))
    right_id: Mapped[int] = mapped_column(ForeignKey("right_table.id"))



class Parent(Base):
    __tablename__ = "left_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    children: Mapped[list["Child"]] = relationship(secondary=parent_child)
    child : Mapped[list["Child"]] = relationship(back_populates="parent")


class Child(Base):
    __tablename__ = "right_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    parent : Mapped[list["Parent"]] = relationship(back_populates="child")


Base.metadata.create_all(engine)









