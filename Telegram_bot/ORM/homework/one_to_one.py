from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship, sessionmaker
from sqlalchemy import ForeignKey, create_engine, String
from faker import Faker

faker = Faker()

engine = create_engine("postgresql+psycopg2://postgres:1@localhost/postgres")
Session = sessionmaker(engine)
session = Session()

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    firstname: Mapped[str] = mapped_column(String)
    lastname: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)
    job: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    diploma: Mapped["Diploma"] = relationship(back_populates="customer")

    def __repr__(self):
        return f"{self.firstname},{self.lastname},{self.job},{self.email},{self.address}"


class Diploma(Base):
    __tablename__ = "diploma"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    customer: Mapped["Customer"] = relationship(back_populates="diploma")


Base.metadata.create_all(engine)

for i in range(100):
    customer = Customer(firstname=faker.first_name(), lastname=faker.last_name(), address=faker.address(),
                        job=faker.job(), email=faker.email())
    session.add(customer)
    session.commit()

# customer = Customer(job=faker.job())
# session.add(customer)
# session.commit()
