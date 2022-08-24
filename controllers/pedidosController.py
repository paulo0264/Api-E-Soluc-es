from models import pedidosModel

def get_all():
  return pedidosModel.get_all()

def get_by_id(id):
  return pedidosModel.get_by_id(id)

def insert():
  return pedidosModel.insert()

def update(id):
  return pedidosModel.update(id)

def delete(id):
  return pedidosModel.soft_delete(id)