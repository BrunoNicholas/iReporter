from flask import jsonify, request

import json

from ..models.db.ireporter import UsersData
from ..models.user import User


class UserController:
    def __init__(self):
        self.sys_users = UsersData()

    def index(self):
        """ this function returns all users """
        try:
            return jsonify(self.sys_users), 200

        except IndexError:
            return jsonify({'error': 'There is an internal problem'}), 500

    def create(self):
        """ this function returns entry to store a user """
        return jsonify({'Message': 'Great, so use the STORE function to create one'}), 200

    def store(self):
        """ this function stores a new user """
        data = request.json
        requested = {
            'name': data.get('name'),
            'email': data.get('email'),
            'password': data.get('password')
        }

        if not all(
                [
                    data.get('name'),
                    data.get('email'),
                    data.get('password')
                ]
        ):
            return jsonify({'error': 'Insufficient field data'}), 400
        else:
            new_user = User(
                requested['name'],
                requested['email'],
                requested['password'],
            )
            self.sys_users.table(new_user.__dict__)
            return jsonify({'Message': 'User added Successfully', 'user': new_user.__dict__}), 200

    def show(self,user_id):
        """ this function returns the details of a specific user """
        try:
            stored_user = [usr for usr in self.sys_users.table() if usr['user_id'] == user_id]
            return jsonify({'User {}'.format(user_id): stored_user[0]}), 200

        except IndexError:
            return jsonify({'error': 'User does not exist!'}), 404

    def edit(self, user_id):
        """ this function returns entry to edit a user's details """
        try:
            stored_user = [usr for usr in self.sys_users.table() if usr['user_id'] == user_id]
            return jsonify({'User {}'.format(user_id): stored_user[0]}), 200

        except IndexError:
            return jsonify({'error': 'User does not exist!'}), 404

    def update(self, user_id):
        """ this function stores an update of a user's details """

        try:
            data = request.json
            stored_user = [usr for usr in self.sys_users.table() if usr['user_id'] == user_id]

            stored_user[0]['name']  = data.get('name')
            stored_user[0]['email'] = data.get('email')
            stored_user[0]['password'] = data.get('password')
            return jsonify({'Message': 'User successfully updated', 'user': stored_user}), 200

        except IndexError:
            return jsonify({'error': 'The user does not exist!'}), 404

    def destroy(self, user_id):
        """ this function reads a user's details and deletes them """
        try:
            stored_user = [usr for usr in self.sys_users.table() if usr['user_id'] == user_id]
            
            self.sys_users.table().remove(user_id)
            return jsonify({'Message': 'User Profile Deleted Successfully!'},{'User {}'.format(user_id):stored_user}), 200

        except IndexError:
            return jsonify({'error': 'Not found, User unavailable'}), 400
