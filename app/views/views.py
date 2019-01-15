from flask import Blueprint, jsonify, request

from ..controllers.user_controller import UserController
from ..controllers.red_flag_controller import RedFlagController
from ..controllers.intervention_controller import InterventionController
from ..models.db.ireporter import UsersData, RedFlagsData, InterventionsData

# from ..models.locator import GeoLocator

JSON_MIME_TYPE = 'application/json'

ireporter_app = Blueprint('ireporter_app', __name__)

all_users = UsersData()
all_redFlags = RedFlagsData()
all_interventions = InterventionsData()

ctr_user 	= UserController()
ctr_inter 	= InterventionController()
ctr_flag 	= RedFlagController()


@ireporter_app.route('/', methods=['GET'])
def index():
    return jsonify({'status':200,'Message': 'Welcome to the iReporter'})


# Red Flag HTTPs
@ireporter_app.route('/red-flags', methods=['GET'])  # returning all
def red_flags():
    return jsonify({'Red-Flags': all_redFlags.table()})


@ireporter_app.route('/red-flags', methods=['POST'])  # saving one
def store_red_flags():
    if request.content_type != JSON_MIME_TYPE:
        return jsonify({'status':406,'error': 'Invalid Content Type - use JSON'}), 406
    return ctr_flag.store()


@ireporter_app.route('/red-flags/create', methods=['GET'])  # creating new
def create_red_flag():
    return jsonify({'status':201,'Message': 'Great, Now use /red-flags to store new user with POST'}), 201


@ireporter_app.route('/red-flags/<int:red_id>', methods=['GET'])  # returning one
def show_red_flag(red_id):
    return ctr_flag.show(red_id)


@ireporter_app.route('/red-flags/<int:red_id>', methods=['PUT'])  # update one
def update_red_flag(red_id):
    if request.content_type != JSON_MIME_TYPE:
        return jsonify({'status':406,'error': 'Invalid Content Type - use JSON'}), 406
    return ctr_flag.update(red_id)


@ireporter_app.route('/red-flags/<int:red_id>', methods=['DELETE'])  # destroy one
def destroy_red_flag(red_id):
    return ctr_flag.destroy(red_id)


@ireporter_app.route('/red-flags/<int:red_id>/edit', methods=['GET'])  # editing one
def edit_red_flag(red_id):
    return ctr_flag.edit(red_id)


# end of red-flag resources
# interventions
@ireporter_app.route('/interventions', methods=['GET'])  # returning all
def interventions():
    return jsonify({'Interventions': all_interventions.table()})


@ireporter_app.route('/interventions', methods=['POST'])  # saving one
def store_intervention():
    if request.content_type != JSON_MIME_TYPE:
        return jsonify({'status':406,'error': 'Invalid Content Type - use JSON'}), 406
    return ctr_inter.store()


@ireporter_app.route('/interventions/create', methods=['GET'])  # creating new
def create_intervention():
    return jsonify({'status':201,'Message': 'Operation working, use STORE to create /interventions'}), 201


@ireporter_app.route('/interventions/<int:int_id>', methods=['GET'])  # returning one
def show_intervention(int_id):
    return ctr_inter.show(int_id)


@ireporter_app.route('/interventions/<int:int_id>', methods=['PUT'])  # update one
def update_intervention(int_id):
    if request.content_type != JSON_MIME_TYPE:
        return jsonify({'status':406,'error': 'Invalid Content Type - use JSON'}), 406
    return ctr_inter.update(int_id)


@ireporter_app.route('/interventions/<int:int_id>', methods=['DELETE'])  # destroy one
def destroy_intervention(int_id):
    return ctr_inter.destroy(int_id)


@ireporter_app.route('/interventions/<int:int_id>/edit', methods=['GET'])  # editing one
def edit_intervention(int_id):
    return ctr_inter.edit(int_id)


# end of interventions
# users
@ireporter_app.route('/users', methods=['GET'])  # returning all
def stored_users():
    return jsonify({'users': all_users.table()})


@ireporter_app.route('/users', methods=['POST'])  # saving one
def store_user():
    if request.content_type != JSON_MIME_TYPE:
        return jsonify({'status':406,'error': 'Invalid Content Type - use JSON'}), 406
    return ctr_user.store()


@ireporter_app.route('/users/create', methods=['GET'])  # creating new
def create_user():
    return jsonify({'status':201,'Message': 'Great, Now use /users to store new user with POST'}), 201


@ireporter_app.route('/users/<int:user_id>', methods=['GET'])  # returning one
def show_user(user_id):
    return ctr_user.show(user_id)
    # return jsonify({'Message': 'User not found or unknown'}), 403


@ireporter_app.route('/users/<int:user_id>/edit', methods=['GET'])  # editing one
def edit_user(user_id):
    return ctr_user.edit(user_id)


@ireporter_app.route('/users/<int:user_id>', methods=['PUT'])  # update one
def update_user(user_id):
    if request.content_type != JSON_MIME_TYPE:
        return jsonify({'status':406,'error': 'Invalid Content Type - use JSON'}), 406
    return ctr_user.update(user_id)


@ireporter_app.route('/users/<int:user_id>', methods=['DELETE'])  # destroy one
def destroy_user(user_id):
    spec_user = ctr_user.destroy(user_id)
    return spec_user


# end of user
