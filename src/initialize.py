from flask import Flask

# Routes
from .routes import VideoWorkerRoutes

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(VideoWorkerRoutes.main, url_prefix='/worker')

    return app
