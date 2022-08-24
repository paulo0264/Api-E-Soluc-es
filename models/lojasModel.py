from datetime import datetime
from config import db
from .tabelas import Lojas
from flask import jsonify, request
import datetime
import jwt
from config import app

def get_all():
  addrs = Lojas.query.all()
  return jsonify([addr.to_json() for addr in addrs]), 200

def get_by_id(id):
  addr = Lojas.query.get(id)
  if addr is None:
    return {"error": "Not found"}, 404
  return jsonify(addr.to_json())

def insert():
  if request.is_json:
    body = request.get_json()
    addr = Lojas (
      nome = body["nome"],
      cpf = body["cpf"],
      email = body["email"]
     

    )
    db.session.add(addr)
    db.session.commit()
    payload = {
      "id": addr.id,
      "exp": datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'])

    return jsonify(token.decode('UTF-8')), 201
  return {"error": "Request must be JSON"}, 415


def update(id):
  if request.is_json:
    body = request.get_json()
    addr = Lojas.query.get(id)
    if addr is None:
      return {"error": "Not found"}, 404
    if("nome" in body):
      addr.nome = body["nome"]
    if("cpf" in body):
      addr.cpf = body["cpf"]
    if("email" in body):
      addr.email = body["email"]
    if("data" in body):
      addr.data = body["data"]
  
    db.session.add(addr)
    db.session.commit()
    return "Atualizado com sucesso", 200
  return {"error": "Request must be JSON"}, 415

def soft_delete(id):
  addr = Lojas.query.get(id)
  if addr is None:
      return {"error": "Not found"}, 404
  addr.active = False   
  db.session.add(addr)
  db.session.commit()
  return "Deletado com sucesso", 200