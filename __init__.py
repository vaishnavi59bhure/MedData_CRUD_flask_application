from flask import Flask
from flask_migrate import Migrate
from errors.error_handlers import register_error_handlers
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# Initialize the Migrate instances
migrate = Migrate()

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:9766194467manU@localhost/pythonproject"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app():
    app = Flask(__name__)

    app.secret_key="None"

    # Load configuration from the Config class
    app.config.from_object(Config)

    # Initialize the extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    from controllers.patient_controller import patient_bp
    # app.register_blueprint(patient_bp)
    app.register_blueprint(patient_bp, url_prefix='/patients')
    # Register Error Handlers
    register_error_handlers(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)