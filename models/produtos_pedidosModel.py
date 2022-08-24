from config import db
from .tabelas import Produtos_Pedidos
from flask import jsonify, request

def get_all():
  produtos_pedidos = Produtos_Pedidos.query.all()
  return jsonify([produto_pedido.to_json() for produto_pedido in produtos_pedidos]), 200

def get_by_id(id):
  produto_pedido = Produtos_Pedidos.query.get(id)
  if produto_pedido is None:
    return {"error": "Not found"}, 404
  return jsonify(produto_pedido.to_json())

def insert():
  if request.is_json:
    body = request.get_json()
    produto_pedido =  Produtos_Pedidos(
    produtos_id = body["produtos_id"]  ,
    pedidos_id = body["pedidos_id"]
    )
    
    db.session.add(produto_pedido)
    db.session.commit()
    return "Cadastrado.", 201
  return {"Erro": "A solicitação deve ser JSON"}, 415


def update(id):
  if request.is_json:
    body = request.get_json()
    produto_pedido = Produtos_Pedidos.query.get(id)
    if produto_pedido is None:
      return {"error": "Not found"}, 404
    if("produto_id" in body):
        produto_pedido.produto_id = body["produto_id"]
        produto_pedido.pedido_id = body["pedido_id"]
    db.session.add(produto_pedido)
    db.session.commit()
    return "Atualizado com sucesso", 200
  return {"Erro": "A solicitação deve ser JSON"}, 415

def soft_delete(id):
  produto_pedido = Produtos_Pedidos.query.get(id)
  if produto_pedido is None:
      return {"error": "Not found"}, 404
  produto_pedido.active = False   
  db.session.add(produto_pedido)
  db.session.commit()
  return "Deletado com sucesso", 200