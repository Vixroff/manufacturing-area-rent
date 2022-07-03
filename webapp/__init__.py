from config import Config

from flask import Flask

from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from webapp.main.views import bp as main_bp
    app.register_blueprint(main_bp)

    return app
