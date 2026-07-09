"""
Theme/Background Model for Custom App Backgrounds
"""

from models import db
from datetime import datetime

class Theme(db.Model):
    __tablename__ = 'themes'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    background_image = db.Column(db.String(500), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Theme {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'background_image': self.background_image,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat()
        }

class GroupTheme(db.Model):
    __tablename__ = 'group_themes'
    
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    background_image = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<GroupTheme for group {self.group_id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'group_id': self.group_id,
            'background_image': self.background_image,
            'created_at': self.created_at.isoformat()
        }
