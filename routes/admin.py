from flask import Blueprint, jsonify, request
from models import Worker
from app import db

admin_routes = Blueprint('admin', __name__, url_prefix='/api')

# Existing GET route
@admin_routes.route('/workers', methods=['GET'])
def get_workers():
    workers = Worker.query.all()
    return jsonify([w.to_dict() for w in workers])

# ✅ New POST route
@admin_routes.route('/workers', methods=['POST'])
def create_worker():
    data = request.json
    new_worker = Worker(
        name=data.get('name'),
        email=data.get('email'),
        service=data.get('service'),
        status=data.get('status', 'Available')
    )
    db.session.add(new_worker)
    db.session.commit()
    return jsonify(new_worker.to_dict()), 201
