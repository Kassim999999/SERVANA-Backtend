from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
import os

from extensions import db
from extensions import jwt as ext_jwt  # keep extensions jwt import for consistency
from routes.admin import admin_routes
from routes.auth import auth_routes
from routes.analytics import analytics_routes

app = Flask(__name__)

from flask_cors import CORS

# Allow your frontend origin with credentials and ensure CORS headers are sent always
CORS(app,
     resources={r"/*": {"origins": "http://localhost:5173"}},
     supports_credentials=True,
     allow_headers=["Content-Type", "Authorization"],
     methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
     expose_headers=["Content-Type", "Authorization"])


# Failsafe: add headers on every response (covers error responses too)
@app.after_request
def add_cors_headers(resp):
    origin = resp.headers.get("Access-Control-Allow-Origin")
    if not origin:
        resp.headers["Access-Control-Allow-Origin"] = "http://localhost:5173"
    resp.headers["Vary"] = "Origin"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    resp.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,PATCH,DELETE,OPTIONS"
    return resp

migrate = Migrate(app, db)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'servana.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- JWT config ---
app.config["JWT_SECRET_KEY"] = "your-secret-key"
app.config["JWT_TOKEN_LOCATION"] = ["headers"]
app.config["JWT_HEADER_NAME"] = "Authorization"
app.config["JWT_HEADER_TYPE"] = "Bearer"

jwt = JWTManager(app)

# Helpful JSON errors
@jwt.unauthorized_loader
def _unauth(msg):
    return jsonify({"error": "Missing or invalid token", "detail": msg}), 401

@jwt.invalid_token_loader
def _invalid(msg):
    return jsonify({"error": "Invalid token", "detail": msg}), 401

@jwt.expired_token_loader
def _expired(h, p):
    return jsonify({"error": "Token expired"}), 401

db.init_app(app)

# Register blueprints
app.register_blueprint(admin_routes)
app.register_blueprint(auth_routes)
app.register_blueprint(analytics_routes)

@app.route('/')
def home():
    return {"message": "Servana API running"}

if __name__ == '__main__':
    from models import Worker, Service, Booking, User
    with app.app_context():
        db.create_all()
    app.run(debug=True)
