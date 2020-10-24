from flask import Flask


def construct_flask_app():
    app = Flask(__name__)
    env = app.config['ENV']
    app.config.from_object('config.{}'.format(env))
    app.app_context().push()
    return app
