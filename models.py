from extensions import db

class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120))
    service = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "service": self.service,
            "status": self.status
        }



class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100))
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Active')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "status": self.status
        }



from datetime import datetime
from sqlalchemy import Numeric
from extensions import db

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    worker_name = db.Column(db.String(100), nullable=False)
    service_name = db.Column(db.String(100), nullable=False)
    scheduled_date = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    amount = db.Column(db.Numeric(10, 2), nullable=True)
    worker_id = db.Column(db.Integer, db.ForeignKey('worker.id', name="fk_booking_worker_id"), nullable=True)



    def to_dict(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "worker_name": self.worker_name,
            "service_name": self.service_name,
            "scheduled_date": self.scheduled_date,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "amount": float(self.amount) if self.amount is not None else 0
        }


from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Add this
    email = db.Column(db.String(100), unique=True)    # Add this
    role = db.Column(db.String(20), default='User')   # Add this
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "is_admin": self.is_admin
        }

