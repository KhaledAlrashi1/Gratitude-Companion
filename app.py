from flask import Flask
import os
import logging

def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)  # Secret key for session management

    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Import and register blueprints
    from routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

    