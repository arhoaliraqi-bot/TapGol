"""
Poll Model
"""

from app import db
from datetime import datetime

class Poll(db.Model):
    __tablename__ = 'polls'
    
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    question = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = db.relationship('User', backref='polls')
    options = db.relationship('PollOption', backref='poll', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Poll {self.question}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'group_id': self.group_id,
            'question': self.question,
            'options': [o.to_dict() for o in self.options],
            'created_at': self.created_at.isoformat()
        }

class PollOption(db.Model):
    __tablename__ = 'poll_options'
    
    id = db.Column(db.Integer, primary_key=True)
    poll_id = db.Column(db.Integer, db.ForeignKey('polls.id'), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    votes = db.Column(db.Integer, default=0)
    
    # Relationships
    voters = db.relationship('User', secondary='poll_votes', backref='voted_options')
    
    def __repr__(self):
        return f'<PollOption {self.text}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'votes': self.votes
        }

# Association table for poll votes
poll_votes = db.Table(
    'poll_votes',
    db.Column('poll_option_id', db.Integer, db.ForeignKey('poll_options.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)
