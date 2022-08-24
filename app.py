from config import app
from flask_cors import CORS
from routes import Lojas, Produtos, Usuarios, Pedidos, Produtos_Pedidos




cors = CORS(app)

if __name__ == '__main__':

  app.register_blueprint(Lojas.app)
  app.register_blueprint(Produtos.app)
  app.register_blueprint(Usuarios.app)
  app.register_blueprint(Pedidos.app)
  app.register_blueprint(Produtos_Pedidos.app)
  app.run(debug=True, host="0.0.0.0", port=8090)