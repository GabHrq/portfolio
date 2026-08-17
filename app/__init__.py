from flask import Flask, request
from flask_babel import Babel

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

def get_locale():
    return request.accept_languages.best_match(
        app.config['LANGUAGES']
    )

babel = Babel(app, locale_selector=get_locale)
from . import routes