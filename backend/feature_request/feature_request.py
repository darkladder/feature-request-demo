from sqlalchemy import Column, String, Integer, Date
from .base import Base

# @see https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
class FeatureRequest(Base):
  __tablename__ = 'feature_request'
  id=Column(Integer, primary_key=True)
  title=Column('title', String(32))
  client=Column('client', String(32))
  client_priority=Column('client_priority', Integer)
  target_date=Column('target_date', Date)
  product_area=Column('product_area', String(32))

  def __init__(self, title, client, client_priority, target_date, product_area):
    self.title = title
    self.client = client
    self.client_priority = client_priority
    self.target_date = target_date
    self.product_area = product_area
    return