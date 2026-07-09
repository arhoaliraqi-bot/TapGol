"""
Theme/Background API Routes
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db
from models.theme import Theme, GroupTheme

themes_bp = Blueprint('themes', __name__)

# User Theme Routes
@themes_bp.route('/user', methods=['GET'])
@jwt_required()
def get_user_themes():
    """Get all themes for current user"""
    user_id = get_jwt_identity()
    
    themes = Theme.query.filter_by(user_id=user_id).all()
    
    return jsonify({
        'themes': [t.to_dict() for t in themes],
        'total': len(themes)
    }), 200

@themes_bp.route('/user', methods=['POST'])
@jwt_required()
def create_user_theme():
    """Create a new user theme/background"""
    user_id = get_jwt_identity()
    data = request.get_json()
    
    if not data.get('name') or not data.get('background_image'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Set all other themes to inactive
    Theme.query.filter_by(user_id=user_id).update({'is_active': False})
    
    new_theme = Theme(
        user_id=user_id,
        name=data['name'],
        background_image=data['background_image'],
        is_active=True
    )
    
    db.session.add(new_theme)
    db.session.commit()
    
    return jsonify(new_theme.to_dict()), 201

@themes_bp.route('/user/<int:theme_id>/activate', methods=['PUT'])
@jwt_required()
def activate_theme(theme_id):
    """Activate a user theme"""
    user_id = get_jwt_identity()
    
    theme = Theme.query.filter_by(id=theme_id, user_id=user_id).first()
    
    if not theme:
        return jsonify({'error': 'Theme not found'}), 404
    
    # Deactivate all other themes
    Theme.query.filter_by(user_id=user_id).update({'is_active': False})
    
    theme.is_active = True
    db.session.commit()
    
    return jsonify(theme.to_dict()), 200

@themes_bp.route('/user/<int:theme_id>', methods=['DELETE'])
@jwt_required()
def delete_user_theme(theme_id):
    """Delete a user theme"""
    user_id = get_jwt_identity()
    
    theme = Theme.query.filter_by(id=theme_id, user_id=user_id).first()
    
    if not theme:
        return jsonify({'error': 'Theme not found'}), 404
    
    db.session.delete(theme)
    db.session.commit()
    
    return jsonify({'message': 'Theme deleted'}), 200

# Group Theme Routes
@themes_bp.route('/group/<int:group_id>', methods=['GET'])
@jwt_required()
def get_group_theme(group_id):
    """Get theme for a group"""
    theme = GroupTheme.query.filter_by(group_id=group_id).first()
    
    if not theme:
        return jsonify({'error': 'No theme for this group'}), 404
    
    return jsonify(theme.to_dict()), 200

@themes_bp.route('/group/<int:group_id>', methods=['POST'])
@jwt_required()
def set_group_theme(group_id):
    """Set theme for a group"""
    data = request.get_json()
    
    if not data.get('background_image'):
        return jsonify({'error': 'Missing background_image'}), 400
    
    # Check if theme exists
    theme = GroupTheme.query.filter_by(group_id=group_id).first()
    
    if theme:
        theme.background_image = data['background_image']
    else:
        theme = GroupTheme(
            group_id=group_id,
            background_image=data['background_image']
        )
        db.session.add(theme)
    
    db.session.commit()
    
    return jsonify(theme.to_dict()), 201

@themes_bp.route('/group/<int:group_id>', methods=['DELETE'])
@jwt_required()
def delete_group_theme(group_id):
    """Delete theme for a group"""
    theme = GroupTheme.query.filter_by(group_id=group_id).first()
    
    if not theme:
        return jsonify({'error': 'No theme for this group'}), 404
    
    db.session.delete(theme)
    db.session.commit()
    
    return jsonify({'message': 'Group theme deleted'}), 200
