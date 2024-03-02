# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UnixValues(db.Model):
    __tablename__ = 'UnixValues'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer, unique=True, nullable=False)

    def to_dict(self):
        return {
            'ID': self.id,
            'Time': self.time
        }