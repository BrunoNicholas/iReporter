from flask import Flask, Blueprint, jsonify, request
from ..http.controllers import *
from ..models import *

JSON_MIME_TYPE = 'application/json'

ireporter_app = Blueprint('ireporter_app', __name__)


@ireporter_app.route('/', methods=['GET'])
def index():
	return (jsonify({'Message' : 'Welcome to the iReporter'}))

# Red Flag HTTPs
@ireporter_app.route('/red-flags') # returning all
def red_flags():
	pass

@ireporter_app.route('/red-flags') # saving one
def store_red_flags():
	pass

@ireporter_app.route('/red-flags/create') #creating new
def create_red_flag():
	pass

@ireporter_app.route('/red-flags/<int:id>') # returning one
def show_red_flag():
	pass

@ireporter_app.route('/red-flags/<int:id>') # update one
def update_red_flag():
	pass

@ireporter_app.route('/red-flags/<int:id>') # destroy one
def destroy_red_flag():
	pass

@ireporter_app.route('/red-flags/<int:id>/edit') # editing one
def edit_red_flag():
	pass

# end of red-flag resources
#interventions
@ireporter_app.route('/interventions') # returning all
def interventions():
	pass

@ireporter_app.route('/interventions') # saving one
def store_intervention():
	pass

@ireporter_app.route('/interventions/create') #creating new
def create_intervention():
	pass

@ireporter_app.route('/interventions/<int:id>') # returning one
def show_intervention():
	pass

@ireporter_app.route('/interventions/<int:id>') # update one
def update_intervention():
	pass

@ireporter_app.route('/interventions/<int:id>') # destroy one
def destroy_intervention():
	pass

@ireporter_app.route('/interventions/<int:id>/edit') # editing one
def edit_intervention():
	pass


#end of interventions
#users
@ireporter_app.route('/users') # returning all
def all_users():
	pass

@ireporter_app.route('/users') # saving one
def store_user():
	pass

@ireporter_app.route('/users/create') #creating new
def create_user():
	pass

@ireporter_app.route('/users/<int:id>') # returning one
def show_user():
	pass

@ireporter_app.route('/users/<int:id>') # update one
def update_user():
	pass

@ireporter_app.route('/users/<int:id>') # destroy one
def destroy_user():
	pass

@ireporter_app.route('/userss/<int:id>/edit') # editing one
def edit_user():
	pass


# end of user	