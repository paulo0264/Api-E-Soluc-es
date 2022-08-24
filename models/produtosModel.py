from config import db
from .tabelas.Lojas import Lojas
from .tabelas import Produtos
from flask import jsonify, request

def get_all():
  produtos = Produtos.query.all()
  print(request.headers)
  return jsonify([produto.to_json() for produto in produtos]), 200

def get_by_id(id):
  produto = Produtos.query.get(id)
  if produto is None:
    return {"error": "Not found"}, 404
  return jsonify(produto.to_json())

def insert():
  if request.is_json:
    body = request.get_json()
    produto =  Produtos(
    #nome = body["nome"],
    #imagem = body["imagem"],
    #valor = body["valor"],
    #quantidade = body["quantidade"],
    #descricao = body["descricao"],
    #lojas_id = body["lojas_id"]  
    )
    if("imagem" in body):
      produto.imagem = body["imagem"]
    if("nome" in body):
      produto.nome = body["nome"]
    if("valor" in body):
      produto.valor = body["valor"]
    if("quantidade" in body):
      produto.quantidade = body["quantidade"]
    if("descricao" in body):
      produto.descricao = body["descricao"]
    if("lojas_id" in body):
        produto.lojas_id = body["lojas_id"]
    
    db.session.add(produto)
    db.session.commit()
    return "Produto Cadastrado.", 201
  return {"Erro": "A solicitação deve ser JSON"}, 415


def update(id):
  if request.is_json:
    body = request.get_json()
    produto = Produtos.query.get(id)
    if produto is None:
      return {"error": "Not found"}, 404
    if("imagem" in body):
      produto.imagem = body["imagem"]
    if("nome" in body):
      produto.nome = body["nome"]
    if("valor" in body):
      produto.valor = body["valor"]
    if("quantidade" in body):
      produto.quantidade = body["quantidade"]
    if("descricao" in body):
      produto.descricao = body["descricao"]
    if("lojas_id" in body):
        produto.lojas_id = body["lojas_id"]
    db.session.add(produto)
    db.session.commit()
    return "Atualizado com sucesso", 200
  return {"Erro": "A solicitação deve ser JSON"}, 415

def soft_delete(id):
  produto = Produtos.query.get(id)
  if produto is None:
      return {"error": "Not found"}, 404
  produto.status = False   
  db.session.add(produto)
  db.session.commit()
  return "Deletado com sucesso", 200

def remover_quantidade(id):
  produto = Produtos.query.get(id)
  if produto is None:
    return {"Erro": "Produto indisponível"}, 404
  produto.quantidade = produto.quantidade-1
  db.session.add(produto)
  db.session.commit()
  return "pedido realizado com sucesso", 200

