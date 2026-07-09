"""
Match Model for Match History
"""

from models import db
from datetime import datetime
from enum import Enum

class MatchStatus(Enum):
    UPCOMING = "upcoming"
    ONGOING = "ongoing"
    FINISHED = "finished"
    CANCELLED = "cancelled"

class Match(db.Model):
    __tablename__ = 'matches'
    
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(50), default=MatchStatus.UPCOMING.value)
    
    team_a_goals = db.Column(db.Integer, default=0)
    team_b_goals = db.Column(db.Integer, default=0)
    mvp_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    
    total_participants = db.Column(db.Integer, default=0)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Match {self.title}>'
    
    def to_dict(self, include_participants=False):
        data = {
            'id': self.id,
            'group_id': self.group_id,
            'title': self.title,
            'description': self.description,
            'date': self.date.isoformat(),
            'location': self.location,
            'status': self.status,
            'team_a_goals': self.team_a_goals,
            'team_b_goals': self.team_b_goals,
            'total_participants': self.total_participants,
            'created_at': self.created_at.isoformat()
        }
        
        return data

match_participants = db.Table(
    'match_participants',
    db.Column('match_id', db.Integer, db.ForeignKey('matches.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)
