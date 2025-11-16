from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy object create gareko, Flask app sanga link garna
db = SQLAlchemy()

def create_app():
    # Flask app banako. __name__ tells Flask where to find files, routes, templates etc.
    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to_do.db'   # SQLite database ko file link
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False           # tracking off gareko (performance ko lagi)
    app.config['SECRET_KEY'] = 'your_secret_key'                   # forms/sessions ko lagi

    # SQLAlchemy init gareko
    db.init_app(app)

    # Import and register routes
    from .routes import main
    app.register_blueprint(main)

    return app
