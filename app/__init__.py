from flask import Flask

from .views.views import fast_food

app = Flask(__name__)
# Registering the Blueprint
app.register_blueprint(ireporter_app, url_prefix='/api/v1')
