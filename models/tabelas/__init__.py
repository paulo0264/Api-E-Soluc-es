from .Lojas import Lojas
from .Produtos import Produtos
from .Usuarios import Usuarios
from .Pedidos import Pedidos
from .Produtos_Pedidos import Produtos_Pedidos
from config import db

__all__ = [
 
  'Lojas'
  'Produtos'
  'Usuarios'
  'Pedidos'
  'Produtos_Pedidos'
]

db.create_all()