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
    if title == None or len(title) == 0:
      raise ValueError('Title must be set')
    
    if client == None or len(client) == 0:
      raise ValueError('Client must be set')
    
    if client_priority == None or int(client_priority) < 1:
      raise ValueError('Client priority must be equal to, or greater than, 1')
    
    if target_date == None:
      raise ValueError('Target date must be set')

    if product_area == None or len(product_area) == 0:
      raise ValueError('Product area must be set')

    '''
    self.title = title
    self.client = client
    self.client_priority = client_priority
    self.target_date = target_date
    self.product_area = product_area
    '''
    return