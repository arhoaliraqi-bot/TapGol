"""
Notification Model
"""

from models import db
from datetime import datetime
from enum import Enum

class NotificationType(Enum):
    MESSAGE = "message"
    POLL_CREATED = "poll_created"
    NEW_MEMBER = "new_member"
    MATCH_CREATED = "match_created"
    MATCH_STARTED = "match_started"
    FOLLOW = "follow"

class Notification(db.Model):
    __tablename__ = 'notifications'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    related_id = db.Column(db.Integer, nullable=True)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Notification {self.type} for user {self.user_id}>'
    
    def mark_as_read(self):
        self.is_read = True
        db.session.commit()
    
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'title': self.title,
            'message': self.message,
            'related_id': self.related_id,
            'is_read': self.is_read,
            'created_at': self.created_at.isoformat()
        }
