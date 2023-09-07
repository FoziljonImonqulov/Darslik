from sqlalchemy import create_engine, String, Integer, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship, mapped_column, Mapped, sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:1@localhost/postgres")
engine.connect()
Session = sessionmaker(engine)
session = Session()

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    last_update: Mapped[str] = mapped_column()


class Language(Base):
    __tablename__ = 'language'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    last_update: Mapped[str] = mapped_column()


class Film(Base):
    __tablename__ = 'film'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[int] = mapped_column(String)
    language_id: Mapped[int] = mapped_column(ForeignKey('language.id'))
    special_features: Mapped[str] = mapped_column(Text)
    description: Mapped[str] = mapped_column(Text)


class Film_category(Base):
    __tablename__ = 'film_category'
    # id: Mapped[int] = mapped_column(primary_key=True)
    film_id: Mapped[int] = mapped_column(ForeignKey("film.id"), primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))
    last_update: Mapped[str] = mapped_column()
    # making_film = relationship(Film)
    # making_category = relationship(Category)


class Actor(Base):
    __tablename__ = 'actor'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[int] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    last_update: Mapped[str] = mapped_column()


class Film_actor(Base):
    __tablename__ = 'film_actor'
    # id: Mapped[int] = mapped_column(primary_key=True)
    film_id: Mapped[int] = mapped_column(ForeignKey('film.id'),primary_key=True)
    actor_id: Mapped[int] = mapped_column(ForeignKey('actor.id'))
    last_update: Mapped[str] = mapped_column()


class Country(Base):
    __tablename__ = 'country'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    country: Mapped[str] = mapped_column()
    last_update: Mapped[str] = mapped_column()


class City(Base):
    __tablename__ = 'city'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    city: Mapped[str] = mapped_column(String)
    country_id: Mapped[int] = mapped_column(ForeignKey('country.id'))
    last_update: Mapped[str] = mapped_column()


class Address(Base):
    __tablename__ = 'address'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    city_id: Mapped[int] = mapped_column(ForeignKey('city.id'))
    phone: Mapped[str] = mapped_column(String)


class Store(Base):
    __tablename = 'store'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    manager_staff_id: Mapped[int] = mapped_column()
    address_id: Mapped[int] = mapped_column(ForeignKey('address.id'))
    last_update: Mapped[str] = mapped_column()


class Customer(Base):
    __tablename__ = 'customer'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[int] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    address_id: Mapped[str] = mapped_column(ForeignKey('address.id'))
    store_id: Mapped[str] = mapped_column(ForeignKey('store.id'))
    email: Mapped[str] = mapped_column(String)


class Inventory(Base):
    __tablename__ = 'inventory'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    film_id: Mapped[int] = mapped_column(ForeignKey('film.id'))
    store_id: Mapped[int] = mapped_column(ForeignKey('store.id'))
    last_update: Mapped[int] = mapped_column()


class Rental(Base):
    __tablename__ = 'rental'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rental_date: Mapped[str] = mapped_column()
    inventory_id: Mapped[str] = mapped_column(ForeignKey('inventory.id'))
    customer_id: Mapped[str] = mapped_column(ForeignKey('customer.id'))
    staff_id: Mapped[str] = mapped_column(ForeignKey('staff.id'))
    return_date: Mapped[str] = mapped_column(String)
    last_update: Mapped[str] = mapped_column(String)


class Payment(Base):
    __tablename__ = 'payment'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_id: Mapped[str] = mapped_column(ForeignKey('customer.id'))
    staff_id: Mapped[str] = mapped_column(ForeignKey('staff.id'))
    rental_id: Mapped[int] = mapped_column(ForeignKey('rental.id'))
    amount: Mapped[str] = mapped_column()
    payment_date: Mapped[str] = mapped_column()


class Staff(Base):
    __tablename__ = 'staff'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[int] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    address_id: Mapped[str] = mapped_column(ForeignKey('address.id'))
    store_id: Mapped[str] = mapped_column(ForeignKey('store.id'))
    username: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(30))
    last_update: Mapped[str] = mapped_column()


Base.metadata.create_all(engine)





# class Post(Base):
#     __tablename__ = 'posts'
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     title: Mapped[str] = mapped_column(__type_pos=String(255))
#     description: Mapped[str] = mapped_column()
#     comments: Mapped[list['Comment']] = relationship(back_populates='post')
#     def __repr__(self):
#         return f"{self.__dict__}"

# class Comment(Base):
#     __tablename__ = 'comments'
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     message: Mapped[str] = mapped_column()
#     post: Mapped['Post'] = relationship(back_populates='comments')
#
#     def __repr__(self):
#         return f"{self.message}"


# association_table = Table(
#     "association_table",
#     Base.metadata,
#     Column("left_id", ForeignKey("left_table.id")),
#     Column("right_id", ForeignKey("right_table.id")),
# )
