from flask import jsonify, request

from ..models.db.ireporter import RedFlagsData
from ..models.red_flag import RedFlag


class RedFlagController:
    """the controller for both endpoints and literating through the red-falgs"""

    def __init__(self):
        self.sys_flags = RedFlagsData()

    def index(self):
        """ the function to return all records """
        try:
            return jsonify(self.sys_flags), 200

        except IndexError:
            return jsonify({'error': 'There is an internal problem'}), 500

    def create(self):
        """ this function returns entry to store a red-flag """
        return jsonify({'Message': 'Great, so use the STORE function to create one'}), 200

    def store(self):
        """ this function stores a new red-flag """
        data = request.json
        requested = {
            'title': data.get('title'),
            'description': data.get('description'),
            'latitude': data.get('latitude'),
            'longitude': data.get('longitude'),
            'attachement': data.get('attachement'),
            'status': data.get('status')
        }

        if not all(
                [
                    data.get('title'),
                    data.get('description'),
                    data.get('latitude'),
                    data.get('longitude'),
                    data.get('attachement'),
                    data.get('status')
                ]
        ):
            return jsonify({'error': 'Insufficient field data'}), 400
        else:
            new_flag = RedFlag(
                requested['title'],
                requested['description'],
                requested['latitude'],
                requested['longitude'],
                requested['attachement'],
                requested['status'],
            )
            self.sys_flags.table(new_flag.__dict__)
            return jsonify({'Message': 'Red-Flag added Successfully', 'Red-Flag': new_flag.__dict__}), 200

    def show(self, red_id):
        """ this function returns the details of a specific red-flag """
        try:
            stored_flag = [flg for flg in self.sys_flags.table() if flg['red_id'] == red_id]
            return jsonify({'Red-Flag {}'.format(red_id): stored_flag[0]}), 200

        except IndexError:
            return jsonify({'error': 'Red-Flag does not exist!'}), 404

    def edit(self, red_id):
        """ this function returns entry to edit a red-flag's details """
        try:
            stored_flag = [flg for flg in self.sys_flags.table() if flg['red_id'] == red_id]
            return jsonify({'Red-Flag {}'.format(red_id): stored_flag[0]}), 200

        except IndexError:
            return jsonify({'error': 'Red-Flag does not exist!'}), 404

    def update(self, red_id):
        """ this function stores an update of a red-flag's details """

        try:
            data = request.json
            stored_flag = [flg for flg in self.sys_flags.table() if flg['red_id'] == red_id]

            stored_flag[0]['title'] = data.get('title')
            stored_flag[0]['description'] = data.get('description')
            stored_flag[0]['latitude'] = data.get('latitude')
            stored_flag[0]['longitude'] = data.get('longitude')
            stored_flag[0]['attachement'] = data.get('attachement')
            stored_flag[0]['status'] = data.get('status')
            return jsonify({'Message': 'Red-Flag successfully updated', 'Red-Flag': stored_flag}), 200

        except IndexError:
            return jsonify({'error': 'The red-flag record does not exist!'}), 404

    def destroy(self, red_id):
        """ this function reads a red-flag's details and deletes them """
        try:
            stored_flag = [flg for flg in self.sys_flags.table() if flg['red_id'] == red_id]

            self.sys_flags.table().remove(red_id)

            return jsonify({'Message': 'Red-Flag record deleted successfully!'},{'Red-Flag {}'.format(red_id):stored_flag}), 200

        except IndexError:
            return jsonify({'error': 'Not found, Red-Flag unavailable'}), 400
