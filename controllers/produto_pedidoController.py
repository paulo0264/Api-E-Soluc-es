from models import produtos_pedidosModel

def get_all():
  return produtos_pedidosModel.get_all()

def get_by_id(id):
  return produtos_pedidosModel.get_by_id(id)

def insert():
  return produtos_pedidosModel.insert()

def update(id):
  return produtos_pedidosModel.update(id)

def delete(id):
  return produtos_pedidosModel.soft_delete(id)