from models import produtosModel

def get_all():
  return produtosModel.get_all()

def get_by_id(id):
  return produtosModel.get_by_id(id)

def insert():
  return produtosModel.insert()

def update(id):
  return produtosModel.update(id)

def delete(id):
  return produtosModel.soft_delete(id)

def remover_quantidade(id):
  return produtosModel.remover_quantidade(id)