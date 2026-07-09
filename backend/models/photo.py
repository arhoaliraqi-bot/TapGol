"""
Photo Model for Photo Management
"""

from models import db
from datetime import datetime

class Photo(db.Model):
    __tablename__ = 'photos'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=True)
    
    filename = db.Column(db.String(255), nullable=False)
    filepath = db.Column(db.String(500), nullable=False)
    file_size = db.Column(db.Integer)
    mime_type = db.Column(db.String(50))
    
    title = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    is_profile_picture = db.Column(db.Boolean, default=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Photo {self.filename}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'match_id': self.match_id,
            'group_id': self.group_id,
            'filename': self.filename,
            'filepath': self.filepath,
            'title': self.title,
            'description': self.description,
            'is_profile_picture': self.is_profile_picture,
            'created_at': self.created_at.isoformat()
        }
