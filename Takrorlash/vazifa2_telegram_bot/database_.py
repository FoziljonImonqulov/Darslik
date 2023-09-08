from faker import Faker
from sqlalchemy import create_engine, String, Column, Integer, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

faker = Faker()
engine = create_engine("postgresql://postgres:1@localhost:5432/postgres")
Session = sessionmaker(engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'  # noqa
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    first_name = Column(String(30))
    last_name = Column(String(30))
    username = Column(String(30))
    is_bot = Column(String(10))
    language = Column(String(10))
    long = Column(String(20))
    lat = Column(String(20))

    # comments = relationship("Comment", back_populates="post")

    def __repr__(self):
        return f"{self.__dict__}"


class Exercise(Base):
    __tablename__ = 'exercises'  # noqa
    id = Column(Integer, primary_key=True, autoincrement=True)
    exercise = Column(String(255))

    # post = relationship("Post", back_populates="comments")

    def __repr__(self):
        return f"{self.__dict__}"


Base.metadata.create_all(engine)
