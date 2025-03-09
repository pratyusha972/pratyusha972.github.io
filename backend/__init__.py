from flask import Flask
from .config import Config
from flask_cors import CORS  # Optional: Enable CORS if needed

def create_app():
    """Factory function to create a Flask app instance."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS (optional)
    CORS(app)

    # Initialize database (if using)
    # db.init_app(app)

    # Import and register Blueprints
    from .routes.routes import backend
    app.register_blueprint(backend, url_prefix="/")

    return app