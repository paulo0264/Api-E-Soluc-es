from config import db

class Produtos_Pedidos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produtos_id = db.Column(db.Integer, db.ForeignKey("produtos.id"))
    pedidos_id = db.Column(db.Integer, db.ForeignKey("pedidos.id"))

    def to_json(self):
       return {
        "id": self.id,
        "produtos_id": self.produtos_id,
        "pedidos_id": self.pedidos_id
        
    }