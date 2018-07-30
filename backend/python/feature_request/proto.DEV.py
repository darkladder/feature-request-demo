# import unittest
# import pprint

# from feature_request import FeatureRequest

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# create an engine
# engine = create_engine('mysql+mysqldb://root:rootpassword@db/feature_request_app')

# create a configured "Session" class
# Session = sessionmaker(bind=engine)

# create a Session
# session = Session()

# fr = FeatureRequest("A title", "A client", 1, "NOW", "Clients")

# print (fr.client)

# feature_requests = session.query(FeatureRequest).all()

from base import Session, engine, Base
from feature_request import FeatureRequest

session = Session()

# 2 - generate database schema
Base.metadata.create_all(engine)

fr = FeatureRequest("A title", "A client", 1, "NOW", "Agents")
session.add(fr)
session.commit()

frs = session.query(FeatureRequest).distinct('product_area')
print('\n### All feature requests:')
for fr in frs:
    print(fr.product_area, fr.target_date)
print('')

session.close()