from flask import Blueprint
from controllers import produto_pedidoController

app=Blueprint('produtos_pedidos', __name__)

@app.route("/produtos_pedidos", methods=["GET"])
def get_produtos_pedidos():
  return produto_pedidoController.get_all()

@app.route("/produtos_pedidos/<int:id>", methods=["GET"])
def get_produtos_pedidos_by_id(id):
  return produto_pedidoController.get_by_id(id)

@app.route("/produtos_pedidos", methods=["POST"])
def insert_produto_pedido():
  return produto_pedidoController.insert()

@app.route("/produtos_pedidos/<int:id>", methods=["PUT"])
def update_produto_pedido(id):
  return produto_pedidoController.update(id)

@app.route("/produtos_pedidos/<int:id>", methods=["DELETE"])
def delete_produtos_pedidos(id):
  return produto_pedidoController.delete(id) 