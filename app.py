from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# SQLite database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///servana.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import routes after db is created
from routes.admin import admin_routes
app.register_blueprint(admin_routes)

@app.route('/')
def home():
    return {"message": "Servana API running"}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
