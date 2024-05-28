#!/usr/bin/python3

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine(
            "mysql://{}:{}@{}/{}".format(
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB"),
            pool_pre_ping=True))


Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData(bind=engine)

if os.getenv("HBNB_ENV") == "test":
    metadata.drop_all()
    session.commit()

obj = session.query(City).all()
for i in obj:
    print(i)