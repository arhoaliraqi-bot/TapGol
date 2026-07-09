"""
User Profiles API Routes
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db
from models.user import User

profiles_bp = Blueprint('profiles', __name__)

@profiles_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_profile(user_id):
    """Get user profile by ID"""
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify(user.to_dict()), 200

@profiles_bp.route('/current', methods=['GET'])
@jwt_required()
def get_current_profile():
    """Get current user's profile"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify(user.to_dict()), 200

@profiles_bp.route('/current', methods=['PUT'])
@jwt_required()
def update_profile():
    """Update current user's profile"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()
    
    if 'name' in data:
        user.name = data['name']
    if 'bio' in data:
        user.bio = data['bio']
    if 'profile_picture' in data:
        user.profile_picture = data['profile_picture']
    
    db.session.commit()
    
    return jsonify(user.to_dict()), 200

@profiles_bp.route('/<int:user_id>/follow', methods=['POST'])
@jwt_required()
def follow_user(user_id):
    """Follow a user"""
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    user_to_follow = User.query.get(user_id)
    
    if not user_to_follow:
        return jsonify({'error': 'User not found'}), 404
    
    if current_user_id == user_id:
        return jsonify({'error': 'Cannot follow yourself'}), 400
    
    if user_to_follow in current_user.following:
        return jsonify({'error': 'Already following this user'}), 400
    
    current_user.following.append(user_to_follow)
    db.session.commit()
    
    return jsonify({'message': 'Successfully followed user'}), 200

@profiles_bp.route('/<int:user_id>/unfollow', methods=['POST'])
@jwt_required()
def unfollow_user(user_id):
    """Unfollow a user"""
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    user_to_unfollow = User.query.get(user_id)
    
    if not user_to_unfollow:
        return jsonify({'error': 'User not found'}), 404
    
    if user_to_unfollow not in current_user.following:
        return jsonify({'error': 'Not following this user'}), 400
    
    current_user.following.remove(user_to_unfollow)
    db.session.commit()
    
    return jsonify({'message': 'Successfully unfollowed user'}), 200
