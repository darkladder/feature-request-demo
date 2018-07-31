from sqlalchemy import Column, String, Integer, Date
from .base import Base

# @see https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
class FeatureRequestORM(Base):
  __tablename__ = 'feature_requests'
  id=Column(Integer, primary_key=True)
  title=Column('title', String(45))
  client=Column('client', String(45))
  description=Column('description', String(255))
  client_priority=Column('client_priority', Integer)
  target_date=Column('target_date', Date)
  product_area=Column('product_area', String(255))

  def __init__(self, title, description, client, client_priority, target_date, product_area):
    if title == None or len(title) == 0:
      raise ValueError('Title must be set')
    else:
      self.title = title
    
    if description == None or len(description) == 0:
      raise ValueError('Description must be set')
    else:
      self.description = description

    if client == None or len(client) == 0:
      raise ValueError('Client must be set')
    else:
      self.client = client
    
    if client_priority == None or int(client_priority) < 1:
      raise ValueError('Client priority must be equal to, or greater than, 1')
    else:
      self.client_priority = client_priority
    
    if target_date == None:
      raise ValueError('Target date must be set')
    else:
      self.target_date = target_date

    if product_area == None or len(product_area) == 0:
      raise ValueError('Product area must be set')
    else:
      self.product_area = product_area
  
    return