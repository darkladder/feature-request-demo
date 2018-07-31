import sys, os

from feature_request import FeatureRequest, Base, Session, engine
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

# Ex. request: http://localhost:5000/api/feature-request/create?title=hello&client=test-client&client_priority=1&target_date=2018-04-28&product_area=agents
@app.route('/api/feature-request', methods=['POST'])
def createFeatureRequest():
  app.logger.debug(request.args)
  # return "Create a feature request"
  # title, client, client_priority, target_date, product_area
  session = Session()

  title = request.args.get('title')
  client = request.args.get('client')
  client_priority = request.args.get('client_priority')
  target_date = request.args.get('target_date')
  product_area = request.args.get('product_area')

  try:
    fr = FeatureRequest(title=title, client=client, client_priority=client_priority, target_date=target_date, product_area=product_area)
  except ValueError as e:
    return str(e), 404

  return "ok"

@app.route('/api/feature-request/<int:feature_request_id>', methods=['GET'])
def getFeatureRequest():
  app.logger.debug(request.args)