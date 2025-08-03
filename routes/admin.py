from flask import Blueprint, jsonify, request
from models import Worker
from extensions import db

admin_routes = Blueprint('admin', __name__, url_prefix='/api')

@admin_routes.route('/workers', methods=['GET'])
def get_workers():
    workers = Worker.query.all()
    return jsonify([w.to_dict() for w in workers])

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


@admin_routes.route('/workers/<int:worker_id>', methods=['DELETE'])
def delete_worker(worker_id):
    worker = Worker.query.get(worker_id)
    if not worker:
        return jsonify({"error": "Worker not found"}), 404

    db.session.delete(worker)
    db.session.commit()
    return jsonify({"message": "Worker deleted"}), 200


@admin_routes.route('/workers/<int:worker_id>', methods=['PUT'])
def update_worker(worker_id):
    worker = Worker.query.get(worker_id)
    if not worker:
        return jsonify({"error": "Worker not found"}), 404

    data = request.json
    worker.name = data.get('name', worker.name)
    worker.email = data.get('email', worker.email)
    worker.service = data.get('service', worker.service)
    worker.status = data.get('status', worker.status)

    db.session.commit()
    return jsonify(worker.to_dict()), 200
