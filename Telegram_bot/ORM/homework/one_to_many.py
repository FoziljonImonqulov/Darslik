from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship, sessionmaker
from sqlalchemy import ForeignKey, create_engine, String
from faker import Faker

faker = Faker()

engine = create_engine("postgresql+psycopg2://postgres:1@localhost/postgres")
Session = sessionmaker(engine)
session = Session()

Base = declarative_base()


class Job(Base):
    __tablename__ = 'job'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[int] = mapped_column(String)
    people: Mapped[list['People']] = relationship()


class People(Base):
    __tablename__ = 'people'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fullname: Mapped[str] = mapped_column(String)
    job_id: Mapped[int] = mapped_column(ForeignKey('job.id'))


Base.metadata.create_all(engine)

# job_title = Job(title=faker.job())
# session.add(job_title)
# session.commit()

for i in range(100):
    person = People(fullname=faker.name(), job_id=1)
    session.add(person)
    session.commit()

