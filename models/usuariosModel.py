from config import db
from .tabelas.Usuarios import Usuarios
from flask import jsonify, request

def get_all():
  usuarios = Usuarios.query.all()
  return jsonify([usuario.to_json() for usuario in usuarios]), 200

def get_by_id(id):
  usuario = Usuarios.query.get(id)
  if usuario is None:
    return {"error": "Not found"}, 404
  return jsonify(usuario.to_json())

def get_by_email(email):
  rest = Usuarios.query.filter_by(email=email).first()
  if rest is None:
    return "Não encontrado", 404
  return jsonify(rest.to_json())

def insert():
  if request.is_json:
    body = request.get_json()
    usuario =  Usuarios(
      nome = body["nome"],
      cpf = body["cpf"],
      cidade = body["cidade"],
      estado = body["estado"],
      bairro = body["bairro"],
      rua = body["rua"],
      numero = body["numero"],
      email = body["email"],
      senha = body["senha"]
      
    )
    
    db.session.add(usuario)
    db.session.commit()
    return "Usuario Cadastrado.", 201
  return {"Erro": "A solicitação deve ser JSON"}, 415


def update(id):
  if request.is_json:
    body = request.get_json()
    usuario = Usuarios.query.get(id)
    if usuario is None:
      return {"error": "Not found"}, 404
    if("nome" in body):
      usuario.nome = body["nome"]
    if("cpf" in body):
      usuario.cpf = body["cpf"]
    if("cidade" in body):
      usuario.cidade = body["cidade"]
    if("estado" in body):
      usuario.estado = body["estado"]
    if("bairro" in body):
        usuario.bairro = body["bairro"]
    if("rua" in body):
        usuario.rua = body["rua"]
    if("numero" in body):
        usuario.numero = body["numero"]
    if("email" in body):
        usuario.email = body["email"]
    if("senha" in body):
        usuario.senha = body["senha"]



    db.session.add(usuario)
    db.session.commit()
    return "Atualizado com sucesso", 200
  return {"Erro": "A solicitação deve ser JSON"}, 415

def soft_delete(id):
  usuario = Usuarios.query.get(id)
  if usuario is None:
      return {"error": "Not found"}, 404
  usuario.active = False   
  db.session.add(usuario)
  db.session.commit()
  return "Deletado com sucesso", 200