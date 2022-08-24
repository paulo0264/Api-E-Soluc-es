from config import db

class Lojas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    cpf = db.Column(db.Integer)
    email = db.Column(db.String(50))
    data = db.Column(db.DateTime, server_default=db.func.now())

    def to_json(self):
       return {
        "id": self.id,
        "nome": self.nome,
        "cpf": self.cpf,
        "email": self.email,
        "data": self.data
    }