from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from extensions import db
from models import User, Worker, Service, Booking
from sqlalchemy import func
from datetime import datetime

analytics_routes = Blueprint('analytics', __name__, url_prefix='/api')

@analytics_routes.route('/analytics', methods=['GET'])
@jwt_required()
def get_analytics():
    # Totals
    total_users = User.query.count()
    total_workers = Worker.query.count()
    total_services = Service.query.count()
    total_jobs = Booking.query.count()
    total_earnings = db.session.query(func.sum(Booking.amount)).scalar() or 0

    # Bookings breakdown
    status_counts = db.session.query(Booking.status, func.count(Booking.id)).group_by(Booking.status).all()
    bookings_overview = {status: count for status, count in status_counts}

    # Revenue history (group by month)
    revenue_by_month = db.session.query(
        func.strftime('%Y-%m', Booking.scheduled_date),
        func.sum(Booking.amount)
    ).group_by(func.strftime('%Y-%m', Booking.scheduled_date)).all()
    revenue_history = [{"month": month, "amount": float(amount)} for month, amount in revenue_by_month]

    # Top providers
    top_providers_data = db.session.query(
        Worker.name,
        func.count(Booking.id)
    ).join(Booking, Booking.worker_id == Worker.id)\
     .filter(Booking.status == 'Completed')\
     .group_by(Worker.id)\
     .order_by(func.count(Booking.id).desc())\
     .limit(5).all()
    top_providers = [{"name": name, "jobs": jobs} for name, jobs in top_providers_data]

    # Recent activity (last 5 bookings)
    recent_activity_data = Booking.query.order_by(Booking.created_at.desc()).limit(5).all()
    recent_activity = [
        f"{b.user_name} booked {b.service_name} with {b.worker_name} - {b.status}"
        for b in recent_activity_data
    ]

    return jsonify({
        "total_users": total_users,
        "total_workers": total_workers,
        "total_services": total_services,
        "total_jobs": total_jobs,
        "total_earnings": total_earnings,
        "bookings_overview": bookings_overview,
        "revenue_history": revenue_history,
        "top_providers": top_providers,
        "recent_activity": recent_activity
    })
