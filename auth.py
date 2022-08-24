import jwt
import datetime
from config import app
from functools import wraps
from models import tabelas
from flask import jsonify, make_response, request
from werkzeug.security import check_password_hash

def token_required(f):
  @wraps(f)
  def decorated(*args, **kwargs):
      token = None
      if 'x-access-token' in request.headers:
          token = request.headers['x-access-token']
      if not token: 
          return jsonify({'message' : 'Token is missing!'}), 401
      try: 
          data = jwt.decode(token, app.config["SECRET_KEY"], options={"verify_signature": False}, algorithms=['SHA256'])
        
      except:
          return jsonify({'message' : 'Token is invalid!'}), 401
      return f( *args, **kwargs)
  return decorated

def login():
  auth = request.authorization
  if not auth or not auth.username or not auth.password:
    return make_response('Could not verify', 401, {"Error": "Login required"})
  rest  = tabelas.Lojas.query.filter_by(email=auth.username).first_or_404()

  if check_password_hash(rest.password, auth.password):
    payload = {
    "public_id": rest.public_id,
    "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=30) 
    }
    token = jwt.encode(payload, app.config["SECRET_KEY"])
    return jsonify({"access_token": token}) 
  return {"Error": "password incorret"} 