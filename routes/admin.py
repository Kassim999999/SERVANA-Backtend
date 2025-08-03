from flask import Blueprint, jsonify

admin_routes = Blueprint('admin', __name__, url_prefix='/api')

# Sample route: Get workers
@admin_routes.route('/workers', methods=['GET'])
def get_workers():
    return jsonify([
        {"id": 1, "name": "Grace Mwende", "service": "House Cleaning", "status": "Available"},
        {"id": 2, "name": "Samuel Otieno", "service": "AC Repair", "status": "Unavailable"}
    ])
