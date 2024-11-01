
from ext.database_ext import db
from ext.flasgeer import sg
from flask import Flask  # type: ignore
import config
from controller.user_controller import usuario_blueprint
from controller.entrada_controller import entrada_blueprint
from controller.saida_controller import saida_blueprint
from controller.tipo_entrada_controller import tipo_entrada_blueprint
from controller.tipo_saida_controller import tipo_saida_blueprint


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}"
        f"@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(usuario_blueprint)
    app.register_blueprint(entrada_blueprint)
    app.register_blueprint(saida_blueprint)
    app.register_blueprint(tipo_saida_blueprint)
    app.register_blueprint(tipo_entrada_blueprint)
    db.init_app(app)
    sg.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
