from flask import Flask, Blueprint

def init_application():
    print("Application initialized.")


def cleanup_application():
    print("Application cleaned up.")


def create_app():
    """
    Creates & initializes a Flask application instance.
    :return:
    """
    app = Flask(__name__, static_folder=None, template_folder=None)

    app.register_blueprint(bp)

    return app


bp = Blueprint('home', __name__)

@bp.get('/')
def home():
    raise Exception("foo")


