from config import db

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    cpf = db.Column(db.String(14))
    cep = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado =db.Column(db.String(50))
    bairro = db.Column(db.String(50))
    rua = db.Column(db.String(50))
    numero = db.Column(db.Integer)
    email = db.Column(db.String(100))
    senha = db.Column(db.String(50))
    

    def to_json(self):
       return {
        "id": self.id,
        "nome": self.nome,
        "cpf": self.cpf,
        "cidade": self.cidade,
        "estado": self.estado,
        "bairro": self.bairro,
        "rua": self.rua,
        "numero": self.numero,
        "email": self.email,
        "senha": self.senha
        
        
    }