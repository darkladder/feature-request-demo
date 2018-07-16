from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('mysql+mysqldb://root:rootpassword@db/feature_request_app')
engine = create_engine('postgresql://postgres:example@db/feature_request')
Session = sessionmaker(bind=engine)

Base = declarative_base()