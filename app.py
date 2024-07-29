from flask import Flask
import os
import logging

def create_app():
    """
    Create and configure an instance of the Flask application.
    """
    app = Flask(__name__)
    app.secret_key = os.urandom(24)  # Secret key for session management

    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Import and register blueprints
    from routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

if __name__ == '__main__':
    # Create the Flask app instance
    app = create_app()

    # Get port from environment variable, default to 5000 if not set
    port = int(os.environ.get('PORT', 5000))

    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=port)