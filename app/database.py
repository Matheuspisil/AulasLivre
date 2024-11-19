from sqlalchemy import create_engine
from sqlalchemy import Sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time

SQLALCHEMY_DATABASE_URL = "sqlite:///./banco.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Sessionlocal = Sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base

