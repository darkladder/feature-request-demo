from sqlalchemy import create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:example@db/postgres')
Session = sessionmaker(bind=engine)

Base = declarative_base()