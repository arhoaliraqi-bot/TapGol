"""
File Upload API Routes
"""

from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from models import db
from models.photo import Photo
import os
from datetime import datetime

uploads_bp = Blueprint('uploads', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
UPLOAD_FOLDER = 'uploads'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@uploads_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload_file():
    """Upload a photo"""
    user_id = get_jwt_identity()
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file.content_length > MAX_FILE_SIZE:
        return jsonify({'error': 'File too large (max 5MB)'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400
    
    # Create upload folder if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    # Generate secure filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
    filename = timestamp + secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    
    # Save file
    file.save(filepath)
    
    # Create photo record in database
    photo = Photo(
        user_id=user_id,
        filename=filename,
        filepath=filepath,
        file_size=file.content_length,
        mime_type=file.content_type,
        title=request.form.get('title'),
        description=request.form.get('description'),
        match_id=request.form.get('match_id'),
        group_id=request.form.get('group_id'),
        is_profile_picture=request.form.get('is_profile_picture', 'false').lower() == 'true'
    )
    
    db.session.add(photo)
    db.session.commit()
    
    return jsonify(photo.to_dict()), 201

@uploads_bp.route('/user/photos', methods=['GET'])
@jwt_required()
def get_user_photos():
    """Get all photos uploaded by current user"""
    user_id = get_jwt_identity()
    
    photos = Photo.query.filter_by(user_id=user_id).order_by(
        Photo.created_at.desc()
    ).all()
    
    return jsonify({
        'photos': [p.to_dict() for p in photos],
        'total': len(photos)
    }), 200

@uploads_bp.route('/match/<int:match_id>/photos', methods=['GET'])
@jwt_required()
def get_match_photos(match_id):
    """Get all photos from a match"""
    photos = Photo.query.filter_by(match_id=match_id).order_by(
        Photo.created_at.desc()
    ).all()
    
    return jsonify({
        'photos': [p.to_dict() for p in photos],
        'total': len(photos)
    }), 200

@uploads_bp.route('/group/<int:group_id>/photos', methods=['GET'])
@jwt_required()
def get_group_photos(group_id):
    """Get all photos from a group"""
    photos = Photo.query.filter_by(group_id=group_id).order_by(
        Photo.created_at.desc()
    ).all()
    
    return jsonify({
        'photos': [p.to_dict() for p in photos],
        'total': len(photos)
    }), 200

@uploads_bp.route('/<int:photo_id>', methods=['DELETE'])
@jwt_required()
def delete_photo(photo_id):
    """Delete a photo"""
    user_id = get_jwt_identity()
    
    photo = Photo.query.filter_by(id=photo_id, user_id=user_id).first()
    
    if not photo:
        return jsonify({'error': 'Photo not found'}), 404
    
    # Delete file from disk
    if os.path.exists(photo.filepath):
        os.remove(photo.filepath)
    
    db.session.delete(photo)
    db.session.commit()
    
    return jsonify({'message': 'Photo deleted'}), 200

@uploads_bp.route('/<int:photo_id>', methods=['PUT'])
@jwt_required()
def update_photo(photo_id):
    """Update photo metadata"""
    user_id = get_jwt_identity()
    data = request.get_json()
    
    photo = Photo.query.filter_by(id=photo_id, user_id=user_id).first()
    
    if not photo:
        return jsonify({'error': 'Photo not found'}), 404
    
    if 'title' in data:
        photo.title = data['title']
    if 'description' in data:
        photo.description = data['description']
    if 'is_profile_picture' in data:
        photo.is_profile_picture = data['is_profile_picture']
    
    db.session.commit()
    
    return jsonify(photo.to_dict()), 200
