from flask import Flask
from extensions import db
import config as cfg


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = cfg.SQLALCHEMY_DATABASE_URI
    db.init_app(app)
    with app.app_context():
        from .provider_a import provider_a
        from .provider_b import provider_b
        from .airflow import airflow

        app.register_blueprint(provider_a.provider_a_bp, url_prefix='/provider_a')
        app.register_blueprint(provider_b.provider_b_bp, url_prefix='/provider_b')
        app.register_blueprint(airflow.airflow_bp, url_prefix='/airflow')

        return app
