from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager


from extensions import db
from routes.admin import admin_routes
from routes.auth import auth_routes




app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///servana.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

db.init_app(app)

app.register_blueprint(admin_routes)
app.register_blueprint(auth_routes)

@app.route('/')
def home():
    return {"message": "Servana API running"}

if __name__ == '__main__':
    from models import Worker
    from models import Service
    from models import Booking
    from models import User

  # import AFTER db is initialized
    with app.app_context():
        db.create_all()
    app.run(debug=True)
