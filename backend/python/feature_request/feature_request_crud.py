from feature_request import FeatureRequestORM, Base, Session, engine, exc

def as_dict(ormResult):
  return {c.name: getattr(ormResult, c.name) for c in ormResult.__table__.columns}

session = Session()

def create_feature_request(title, description, client, client_priority, target_date, product_area):
  try:
    fr = FeatureRequestORM(title=title, description=description, client=client, client_priority=client_priority, target_date=target_date, product_area=product_area)
    session.add(fr)
    session.commit()
    
    print (str(fr.id))
    return str(fr.id)

  except exc.SQLAlchemyError as e:
    raise ValueError(e)

def update_feature_request(id, title=None, description=None, client=None, client_priority=None, target_date=None, product_area=None):
  try:

    fr = session.query(FeatureRequestORM).filter(FeatureRequestORM.id == id).one()

    if len(title) > 0:
      fr.title = title
    
    if len(description) > 0:
      fr.description = description
    
    if len(client) > 0:
      fr.client = client
    
    if len(client_priority) > 0:
      fr.client_priority = client_priority
    
    if len(target_date) > 0:
      fr.target_date = target_date
    
    if len(product_area) > 0:
      fr.product_area = product_area

    session.commit()

    return id

  except exc.SQLAlchemyError as e:
    raise ValueError(e)

def get_single_feature_request(id):
  try:
    fr = session.query(FeatureRequestORM).filter(FeatureRequestORM.id == id).one()

    return as_dict(fr)
    
  except exc.SQLAlchemyError as e:
    raise ValueError(e)

def get_all_feature_requests():
  try:
    # TODO: Order by client priority
    frs = session.query(FeatureRequestORM).order_by(FeatureRequestORM.client_priority).order_by(FeatureRequestORM.target_date).all()

    dictRows = []

    for fr in frs:
      dictRows.append(as_dict(fr))

    return dictRows
  
  except exc.SQLAlchemyError as e:
    raise ValueError(e)

def delete_feature_request(id):
  try:
    fr = session.query(FeatureRequestORM).filter(FeatureRequestORM.id == id).one()
    session.delete(fr)
    session.commit()

    return 'ok'
    
  except exc.SQLAlchemyError as e:
    raise ValueError(e)

def get_product_areas():
  '''
  Retrieves a list of product areas.
  '''
  try:
    pasdb = session.query(FeatureRequestORM.product_area).distinct('product_area').all()
    
    product_areas = []

    for padb in pasdb:
      product_areas.append(padb[0])

    return product_areas
  
  except exc.SQLAlchemyError as e:
    raise ValueError(e)

def get_clients():
  '''
  Retrieves a list of clients.
  '''
  try:
    clientsdb = session.query(FeatureRequestORM.client).distinct('client').all()

    clients = []

    for clientdb in clientsdb:
      clients.append(clientdb[0])
    
    return clients
  
  except exc.SQLAlchemyError as e:
    raise ValueError(e)