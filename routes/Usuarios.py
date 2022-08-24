from flask import Blueprint
from controllers import usuariosController

app=Blueprint('usuarios', __name__)

@app.route("/usuarios", methods=["GET"])
def get_usuarios():
  return usuariosController.get_all()

@app.route("/usuarios/<int:id>", methods=["GET"])
def get_usuarios_by_id(id):
  return usuariosController.get_by_id(id)

@app.route("/usuarios", methods=["POST"])
def insert_usuario():
  return usuariosController.insert()

@app.route("/usuarios/<int:id>", methods=["PUT"])
def update_usuario(id):
  return usuariosController.update(id)

@app.route("/usuarios/email/<email>" , methods=["GET"])
def get_usuarios_by_email(email):
  return usuariosController.get_by_email(email)

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def delete_usuarios(id):
  return usuariosController.delete(id) 