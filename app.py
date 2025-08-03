from flask import Flask
from flask_cors import CORS
from extensions import db
from routes.admin import admin_routes

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///servana.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(admin_routes)

@app.route('/')
def home():
    return {"message": "Servana API running"}

if __name__ == '__main__':
    from models import Worker
    from models import Service
    from models import Booking

  # import AFTER db is initialized
    with app.app_context():
        db.create_all()
    app.run(debug=True)
