from flask import Blueprint
from controllers import pedidosController

app=Blueprint('pedidos', __name__)

@app.route("/pedidos", methods=["GET"])
def get_pedidos():
  return pedidosController.get_all()

@app.route("/pedidos/<int:id>", methods=["GET"])
def get_pedidos_by_id(id):
  return pedidosController.get_by_id(id)

@app.route("/pedidos", methods=["POST"])
def insert_pedidos():
  return pedidosController.insert()

@app.route("/pedidos/<int:id>", methods=["PUT"])
def update_pedidos(id):
  return pedidosController.update(id)

@app.route("/pedidos/<int:id>", methods=["DELETE"])
def delete_pedidos(id):
  return pedidosController.delete(id) 