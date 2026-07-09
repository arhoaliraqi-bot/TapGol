"""
Match History API Routes
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db
from models.match import Match, match_participants
from datetime import datetime

matches_bp = Blueprint('matches', __name__)

@matches_bp.route('/group/<int:group_id>', methods=['GET'])
@jwt_required()
def get_group_matches(group_id):
    """Get all matches for a group"""
    matches = Match.query.filter_by(group_id=group_id).order_by(
        Match.date.desc()
    ).all()
    
    return jsonify({
        'matches': [m.to_dict() for m in matches],
        'total': len(matches)
    }), 200

@matches_bp.route('/user', methods=['GET'])
@jwt_required()
def get_user_match_history():
    """Get current user's match history"""
    user_id = get_jwt_identity()
    
    # Query matches where user is a participant
    matches = db.session.query(Match).join(
        match_participants
    ).filter(
        match_participants.c.user_id == user_id
    ).order_by(Match.date.desc()).all()
    
    return jsonify({
        'matches': [m.to_dict() for m in matches],
        'total': len(matches)
    }), 200

@matches_bp.route('', methods=['POST'])
@jwt_required()
def create_match():
    """Create a new match"""
    user_id = get_jwt_identity()
    data = request.get_json()
    
    if not data.get('group_id') or not data.get('title') or not data.get('date'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        match_date = datetime.fromisoformat(data['date'])
    except ValueError:
        return jsonify({'error': 'Invalid date format'}), 400
    
    new_match = Match(
        group_id=data['group_id'],
        title=data['title'],
        description=data.get('description'),
        date=match_date,
        location=data.get('location')
    )
    
    db.session.add(new_match)
    db.session.commit()
    
    return jsonify(new_match.to_dict()), 201

@matches_bp.route('/<int:match_id>', methods=['GET'])
@jwt_required()
def get_match(match_id):
    """Get match details"""
    match = Match.query.get(match_id)
    
    if not match:
        return jsonify({'error': 'Match not found'}), 404
    
    return jsonify(match.to_dict(include_participants=True)), 200

@matches_bp.route('/<int:match_id>/join', methods=['POST'])
@jwt_required()
def join_match(match_id):
    """Join a match"""
    user_id = get_jwt_identity()
    match = Match.query.get(match_id)
    
    if not match:
        return jsonify({'error': 'Match not found'}), 404
    
    user = db.session.query(User).get(user_id)
    
    if user in match.participants:
        return jsonify({'error': 'Already joined this match'}), 400
    
    match.participants.append(user)
    match.total_participants = len(match.participants)
    db.session.commit()
    
    return jsonify({
        'message': 'Successfully joined match',
        'total_participants': match.total_participants
    }), 200

@matches_bp.route('/<int:match_id>/leave', methods=['POST'])
@jwt_required()
def leave_match(match_id):
    """Leave a match"""
    user_id = get_jwt_identity()
    match = Match.query.get(match_id)
    
    if not match:
        return jsonify({'error': 'Match not found'}), 404
    
    user = db.session.query(User).get(user_id)
    
    if user not in match.participants:
        return jsonify({'error': 'Not joined this match'}), 400
    
    match.participants.remove(user)
    match.total_participants = len(match.participants)
    db.session.commit()
    
    return jsonify({
        'message': 'Successfully left match',
        'total_participants': match.total_participants
    }), 200

from models.user import User
