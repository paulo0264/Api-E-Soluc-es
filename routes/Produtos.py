from flask import Blueprint
from controllers import produtosController
from auth import token_required

app=Blueprint('produtos', __name__)

@app.route("/produtos", methods=["GET"])

def get_produtos():
  return produtosController.get_all()

@app.route("/produtos/<int:id>", methods=["GET"])
def get_produtos_by_id(id):
  return produtosController.get_by_id(id)

@app.route("/produtos", methods=["POST"])

def insert_produto():
  return produtosController.insert()

@app.route("/produtos/<int:id>", methods=["PUT"])
def update_produto(id):
  return produtosController.update(id)

@app.route("/produtos/<int:id>", methods=["DELETE"])
def delete_produtos(id):
  return produtosController.delete(id) 

@app.route("/quantidade/<int:id>", methods=["PUT"])
def remover_quantidade(id):
  return produtosController.remover_quantidade(id) 