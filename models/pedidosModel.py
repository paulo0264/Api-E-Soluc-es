from config import db
from .tabelas import Pedidos
from flask import jsonify, request

def get_all():
  pedidos = Pedidos.query.all()
  return jsonify([pedido.to_json() for pedido in pedidos]), 200

def get_by_id(id):
  pedido = Pedidos.query.get(id)
  if pedido is None:
    return {"error": "Not found"}, 404
  return jsonify(pedido.to_json())

def insert():
  if request.is_json:
    body = request.get_json()
    pedido =  Pedidos(
      quantidade = body["quantidade"],
      valor_total = body["valor_total"],
      data = body["data"],
      usuarios_id = body["usuarios_id"]  
    )
    
    db.session.add(pedido)
    db.session.commit()
    return "Pedido Cadastrado.", 201
  return {"Erro": "A solicitação deve ser JSON"}, 415


def update(id):
  if request.is_json:
    body = request.get_json()
    pedido = Pedidos.query.get(id)
    if pedido is None:
      return {"error": "Not found"}, 404
    if("quantidade" in body):
      pedido.quantidade = body["quantidade"]
    if("valor_total" in body):
      pedido.valor_total = body["valor_total"]
    if("data" in body):
      pedido.quantidade = body["data"]
    if("usuarios_id" in body):
        pedido.usuarios_id = body["usuarios_id"]
    db.session.add(pedido)
    db.session.commit()
    return "Atualizado com sucesso", 200
  return {"Erro": "A solicitação deve ser JSON"}, 415

def soft_delete(id):
  pedido = Pedidos.query.get(id)
  if pedido is None:
      return {"error": "Not found"}, 404
  pedido.active = False   
  db.session.add(pedido)
  db.session.commit()
  return "Deletado com sucesso", 200