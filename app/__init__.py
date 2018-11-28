from flask import Flask

from .views.views import ireporter_app

app = Flask(__name__)

# Registering the Blueprint to version the API as v1
app.register_blueprint(ireporter_app, url_prefix='/api/v1')
