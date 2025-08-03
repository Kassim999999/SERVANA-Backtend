from flask import Flask
from flask_cors import CORS
from routes.admin import admin_routes

app = Flask(__name__)
CORS(app)  # Allow React frontend to talk to this backend

# Register routes
app.register_blueprint(admin_routes)

@app.route('/')
def home():
    return {"message": "Servana API running"}

if __name__ == '__main__':
    app.run(debug=True)
