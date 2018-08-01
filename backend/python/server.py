import sys, os
import json
from feature_request import feature_request_crud
from flask import Flask, session, redirect, url_for, escape, request, send_from_directory

BACKEND_DIR = os.path.dirname(os.path.realpath(__file__))
FRONTEND_DIR = os.path.join(BACKEND_DIR, '..', '..', 'frontend', 'public')

app = Flask(__name__)

# Front-end web & asset routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def index(path):
  app.logger.debug(path)
  return send_from_directory(FRONTEND_DIR, path)

# Ex. request: http://localhost:5000/api/feature-request?title=hello&description=abcde&client=test-client&client_priority=1&target_date=2018-04-28&product_area=agents
@app.route('/api/feature-request', methods=['POST'])
def createFeatureRequest():
  app.logger.debug(request.args)
  # return "Create a feature request"
  # title, client, client_priority, target_date, product_area

  title = request.args.get('title')
  description = request.args.get('description')
  client = request.args.get('client')
  client_priority = request.args.get('client_priority')
  target_date = request.args.get('target_date')
  product_area = request.args.get('product_area')

  try:
    frId = feature_request_crud.create_feature_request(title, description, client, client_priority, target_date, product_area)

    return (str(frId))

  except ValueError as e:
    return str(e), 404

# Ex. request: http://localhost:5000/api/feature-request?id=8&title=hello+there&description=abcde&client=test-client&client_priority=1&target_date=2018-04-28&product_area=agents
# PUT is the normal method to update w/ but allow POST to work here in case the client doesn't support PUT
@app.route('/api/feature-request/<int:feature_request_id>', methods=['PUT', 'POST'])
def updateFeatureRequest(feature_request_id):
  app.logger.debug(request.args)
  # return "Create a feature request"
  # title, client, client_priority, target_date, product_area

  title = request.args.get('title')
  description = request.args.get('description')
  client = request.args.get('client')
  client_priority = request.args.get('client_priority')
  target_date = request.args.get('target_date')
  product_area = request.args.get('product_area')

  try:

    frId = feature_request_crud.update_feature_request(id=feature_request_id, title=title, description=description, client=client, client_priority=client_priority, target_date=target_date, product_area=product_area)

    return (str(frId))

  except ValueError as e:
    return str(e), 404

@app.route('/api/feature-request/clients', methods=['GET'])
def getClients():
  try:
    clients = feature_request_crud.get_clients()

    return json.dumps(clients, indent=4)
  
  except ValueError as e:
    return str(e), 404

@app.route('/api/feature-request/product-areas', methods=['GET'])
def getProductAreas():
  try:
    product_areas = feature_request_crud.get_product_areas()

    return json.dumps(product_areas, indent=4)
  
  except ValueError as e:
    return str(e), 404


@app.route('/api/feature-request/<int:feature_request_id>', methods=['GET'])
def getSingleFeatureRequest(feature_request_id):
  try:

    fr = feature_request_crud.get_single_feature_request(feature_request_id)

    return json.dumps(fr, indent=4, sort_keys=False, default=str)
    
  except ValueError as e:
    return str(e), 404

@app.route('/api/feature-requests', methods=['GET'])
def getAllFeatureRequests():
  try:
    # TODO: Order by client priority
    frs = feature_request_crud.get_all_feature_requests()

    return json.dumps(frs, indent=4, sort_keys=False, default=str)
  
  except ValueError as e:
    return str(e), 404

@app.route('/api/feature-request/<int:feature_request_id>', methods=['DELETE'])
def deleteFeatureRequest(feature_request_id):
  try:
    fr = feature_request_crud.delete_feature_request(feature_request_id)

    return 'ok'
    
  except ValueError as e:
    return str(e), 404
