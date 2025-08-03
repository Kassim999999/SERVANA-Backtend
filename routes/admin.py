from flask import Blueprint, jsonify, request
from models import Worker
from extensions import db
from models import Service
from models import Booking

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


@admin_routes.route('/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    return jsonify([s.to_dict() for s in services])

@admin_routes.route('/services', methods=['POST'])
def create_service():
    data = request.json
    service = Service(
        name=data.get('name'),
        category=data.get('category'),
        price=data.get('price'),
        status=data.get('status', 'Active')
    )
    db.session.add(service)
    db.session.commit()
    return jsonify(service.to_dict()), 201

@admin_routes.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        return jsonify({"error": "Service not found"}), 404

    data = request.json
    service.name = data.get('name', service.name)
    service.category = data.get('category', service.category)
    service.price = data.get('price', service.price)
    service.status = data.get('status', service.status)

    db.session.commit()
    return jsonify(service.to_dict()), 200

@admin_routes.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        return jsonify({"error": "Service not found"}), 404

    db.session.delete(service)
    db.session.commit()
    return jsonify({"message": "Service deleted"}), 200


# GET all bookings
@admin_routes.route('/bookings', methods=['GET'])
def get_bookings():
    bookings = Booking.query.order_by(Booking.created_at.desc()).all()
    return jsonify([b.to_dict() for b in bookings])

# POST a new booking
@admin_routes.route('/bookings', methods=['POST'])
def create_booking():
    data = request.json
    booking = Booking(
        user_name=data.get('user_name'),
        worker_name=data.get('worker_name'),
        service_name=data.get('service_name'),
        scheduled_date=data.get('scheduled_date'),
        status=data.get('status', 'Pending')
    )
    db.session.add(booking)
    db.session.commit()
    return jsonify(booking.to_dict()), 201

# PUT (edit/update)
@admin_routes.route('/bookings/<int:booking_id>', methods=['PUT'])
def update_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404

    data = request.json
    booking.user_name = data.get('user_name', booking.user_name)
    booking.worker_name = data.get('worker_name', booking.worker_name)
    booking.service_name = data.get('service_name', booking.service_name)
    booking.scheduled_date = data.get('scheduled_date', booking.scheduled_date)
    booking.status = data.get('status', booking.status)

    db.session.commit()
    return jsonify(booking.to_dict()), 200

# DELETE booking
@admin_routes.route('/bookings/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404

    db.session.delete(booking)
    db.session.commit()
    return jsonify({"message": "Booking deleted"}), 200
