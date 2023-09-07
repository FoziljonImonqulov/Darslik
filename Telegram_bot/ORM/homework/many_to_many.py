from __future__ import annotations

from sqlalchemy import Column, create_engine
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, sessionmaker
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

engine = create_engine("postgresql+psycopg2://postgres:1@localhost/postgres")
Session = sessionmaker(engine)
session = Session()


class Base(DeclarativeBase):
    pass


association_table = Table(
    "association_table",
    Base.metadata,
    Column("left_id", ForeignKey("left_table.id")),
    Column("right_id", ForeignKey("right_table.id")),
)


class Parent(Base):
    __tablename__ = "left_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    children: Mapped[list[Child]] = relationship(secondary=association_table)


class Child(Base):
    __tablename__ = "right_table"

    id: Mapped[int] = mapped_column(primary_key=True)