from flask import Blueprint
from controllers import lojascontroller

app=Blueprint('lojas', __name__)

@app.route("/lojas", methods=["GET"])
def get_usuarios():
  return lojascontroller.get_all()

@app.route("/lojas/<int:id>", methods=["GET"])
def get_usuarios_by_id(id):
  return lojascontroller.get_by_id(id)

@app.route("/lojas", methods=["POST"])
def insert_addr():
  return lojascontroller.insert()

@app.route("/lojas/<int:id>", methods=["PUT"])
def update_addr(id):
  return lojascontroller.update(id)

@app.route("/lojas/<int:id>", methods=["DELETE"])
def delete_usuarios(id):
  return lojascontroller.delete(id) 