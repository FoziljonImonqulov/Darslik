import random

from faker import Faker
from sqlalchemy import create_engine, String, Column, Integer, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

faker = Faker()

engine = create_engine("postgresql+psycopg2://postgres:1@localhost/postgres")
Session = sessionmaker(engine)
session = Session()

Base = declarative_base()


class Post(Base):
    __tablename__ = 'posts'  # noqa
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_title = Column(String(255))
    description = Column(Text)
    comments = relationship("Comment", back_populates="post")

    def __repr__(self):
        return f"{self.__dict__}"


class Comment(Base):
    __tablename__ = 'comments'  # noqa
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(ForeignKey('posts.id'))
    message = Column(Text)
    post = relationship("Post", back_populates="comments")

    def __repr__(self):
        return f"{self.message}"


Base.metadata.create_all(engine)
# for i in range(1, 101):
#     post = Post(title=faker.sentence(), description=faker.text())
#     session.add(post)
#
# session.commit()
# session.add_all([Post(title=faker.sentence(), description=faker.text()) for _ in range(1, 101)])
# session.add_all([Comment(post_id=random.randrange(1, 101), message=faker.text()) for _ in range(1, 1001)])
# session.commit()

"""
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# 1. Create a SQLAlchemy engine and connect to the database
engine = create_engine('your_database_connection_string_here')

# 2. Reflect the existing table
metadata = MetaData()
existing_table = Table('your_existing_table_name', metadata, autoload=True, autoload_with=engine)

# 3. Define the new column
new_column = Column('new_column_name', Integer)

# 4. Add the new column to the table
existing_table.create_column(new_column)

# 5. Commit the changes to the database (if needed)
engine.commit()

"""
"""
from sqlalchemy import create_engine, MetaData, Table, Column, Integer

# 1. Create a SQLAlchemy engine and connect to the database
engine = create_engine('your_database_connection_string_here')

# 2. Reflect the existing table
metadata = MetaData()
existing_table = Table('your_existing_table_name', metadata, autoload=True, autoload_with=engine)

# 3. Define a new column with the desired name
new_column = Column('new_column_name', Integer)

# 4. Copy data from the old column to the new one
update_stmt = existing_table.update().values(new_column_name=new_column)
engine.execute(update_stmt)

# 5. Remove the old column
existing_table.c.old_column_name.drop()

# 6. Commit the changes (if using transactions)
# engine.commit()

"""

"""
from sqlalchemy import create_engine, MetaData, Table, text

# 1. Create a SQLAlchemy engine and connect to the database
engine = create_engine('your_database_connection_string_here')

# 2. Reflect the existing (old) table
metadata = MetaData()
old_table = Table('old_table_name', metadata, autoload=True, autoload_with=engine)

# 3. Define the new table with the desired name
new_table_name = 'new_table_name'
new_table = old_table.rename(new_table_name)

# 4. Copy data from the old table to the new one
copy_data_sql = text(f"INSERT INTO {new_table_name} SELECT * FROM {old_table.name}")
engine.execute(copy_data_sql)

# 5. Drop the old table
drop_table_sql = text(f"DROP TABLE {old_table.name}")
engine.execute(drop_table_sql)

# 6. Commit the changes (if using transactions)
# engine.commit()

"""

