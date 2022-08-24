from config import db

class Pedidos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer)
    valor_total = db.Column(db.Numeric(10,2))
    data = db.Column(db.DateTime, server_default=db.func.now())
    usuarios_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"))

    def to_json(self):
       return {
        "id": self.id,
        "quantidade": self.quantidade,
        "valor_total": self.valor_total,
        "data": self.data,
        "usuarios_id": self.usuarios_id
    }