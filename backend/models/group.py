"""
Group Model
"""

from models import db
from datetime import datetime

class Group(db.Model):
    __tablename__ = 'groups'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    group_picture = db.Column(db.String(255), nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Group {self.name}>'
    
    def to_dict(self, include_members=False):
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'group_picture': self.group_picture,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat()
        }
        
        return data

group_members = db.Table(
    'group_members',
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)
