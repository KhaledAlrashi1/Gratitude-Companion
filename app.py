from flask import Flask
import logging
from routes import main
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(main)

# Configure logging
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    app.run(debug=True)