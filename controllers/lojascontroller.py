from models import lojasModel

def get_all():
  return lojasModel.get_all()

def get_by_id(id):
  return lojasModel.get_by_id(id)

def insert():
  return lojasModel.insert()

def update(id):
  return lojasModel.update(id)

def delete(id):
  return lojasModel.soft_delete(id)