from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = create_engine('sqlite:///database_app/database.db')

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    email = Column("email", String, unique=True, nullable=False)
    password = Column("password", String, nullable=False)
    active = Column("active", Boolean, default=True)
    admin = Column("admin", Boolean, default=False)
    roles = Column("roles", String, default="user")

    def __init__(self, name, email, password, active=True, admin=False, roles="user"):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin
