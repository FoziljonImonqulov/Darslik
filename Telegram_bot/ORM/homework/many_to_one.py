from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship, sessionmaker
from sqlalchemy import ForeignKey, create_engine, String
from faker import Faker

faker = Faker()

engine = create_engine("postgresql+psycopg2://postgres:1@localhost/postgres")
Session = sessionmaker(engine)
session = Session()

Base = declarative_base()


class Property(Base):
    __tablename__ = "property"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)
    phone_number: Mapped[str] = mapped_column(String)
    person_id: Mapped[int] = mapped_column(ForeignKey("person.id"))
    person: Mapped["Person"] = relationship()


class Person(Base):
    __tablename__ = "person"

    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[int] = mapped_column(String)


Base.metadata.create_all(engine)

# job_title = Person(fullname=faker.name())
# session.add(job_title)
# session.commit()
#
for i in range(100):
    person = Property(email=faker.email(), address=faker.address(), phone_number = faker.phone_number(), person_id=1)
    session.add(person)
    session.commit()

