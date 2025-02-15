import os

from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'sqlite.db'),
    )
    from . import db
    db.init_app(app)

    from . import yaminabe
    app.register_blueprint(yaminabe.bp)

    from . import ingredient
    app.register_blueprint(ingredient.bp)

    return app
