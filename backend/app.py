"""
TapGol Backend - Main Application Entry Point
"""

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'postgresql://user:password@localhost:5432/tapgol'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-secret-key-change-in-production')

# Initialize extensions
db = SQLAlchemy(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
jwt = JWTManager(app)

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health():
    return {'status': 'OK', 'message': 'TapGol Backend is running'}, 200

# Blueprint imports (will be added later)
# from routes import auth_bp, groups_bp, messages_bp, polls_bp
# app.register_blueprint(auth_bp, url_prefix='/api/auth')
# app.register_blueprint(groups_bp, url_prefix='/api/groups')
# app.register_blueprint(messages_bp, url_prefix='/api/messages')
# app.register_blueprint(polls_bp, url_prefix='/api/polls')

if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    
    # Run the app
    app.run(
        debug=os.getenv('FLASK_ENV') == 'development',
        host='0.0.0.0',
        port=int(os.getenv('PORT', 5000))
    )