from flask import Flask
from decouple import config


app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

from core import routes, custom_filters, playlist