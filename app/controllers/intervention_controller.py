from flask import jsonify, request

from ..models.intervention import Intervention
from ..models.db.ireporter import InterventionsData


class InterventionController:
    """This is the controller for the intervention endpoints"""

    def __init__(self):
        self.sys_interventions = InterventionsData()

    def index(self):
        """ the function to return all intervention records """
        try:
            return jsonify(self.sys_interventions), 200

        except IndexError:
            return jsonify({'error': 'There is an internal problem'}), 500

    def create(self):
        """ this function returns entry to store an intervention """
        return jsonify({'Message': 'Great, so use the STORE function to create one'}), 200

    def store(self):
        """ this function stores a new intervention record """
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
            new_interv = Intervention(
                requested['title'],
                requested['description'],
                requested['latitude'],
                requested['longitude'],
                requested['attachement'],
                requested['status'],
            )
            self.sys_interventions.table(new_interv.__dict__)
            return jsonify({'Message': 'Intervention added Successfully', 'intervention': new_interv.__dict__}), 200

    def show(self, int_id):
        """ this function returns the details of a specific intervention """
        try:
            saved_interv = [interv for interv in self.sys_interventions.table() if interv['int_id'] == int_id]
            return jsonify({'Intervention {}'.format(int_id): saved_interv[0]}), 200

        except IndexError:
            return jsonify({'error': 'Intervention record does not exist!'}), 404

    def edit(self, int_id):
        """ this function returns entry to edit an intervention's details """
        try:
            saved_interv = [interv for interv in self.sys_interventions.table() if interv['int_id'] == int_id]
            return jsonify({'intervention {}'.format(int_id): saved_interv[0]}), 200

        except IndexError:
            return jsonify({'error': 'Intervention does not exist!'}), 404

    def update(self, int_id):
        """ this function stores an update of an intervention's details """

        try:
            data = request.json
            saved_interv = [interv for interv in self.sys_interventions.table() if interv['int_id'] == int_id]

            saved_interv[0]['title'] = data.get('title')
            saved_interv[0]['description'] = data.get('description')
            saved_interv[0]['latitude'] = data.get('latitude')
            saved_interv[0]['longitude'] = data.get('longitude')
            saved_interv[0]['attachement'] = data.get('attachement')
            saved_interv[0]['status'] = data.get('status')
            return jsonify({'Message': 'Intervention successfully updated!', 'Intervention': saved_interv}), 200

        except IndexError:
            return jsonify({'error': 'The intervention record does not exist!'}), 404

    def destroy(self, int_id):
        """ this function reads an intervention's details and deletes them """
        try:
            saved_interv = [interv for interv in self.sys_interventions.table() if int(interv['int_id']) == int(int_id])
            
            self.sys_interventions.table().remove(int_id)
            return jsonify({'Message': 'Intervention record deleted successfully!'},{'Intervention {}'.format(int_id):saved_interv}), 200

        except IndexError:
            return jsonify({'error': 'Not found, intervention unavailable!'}), 400

            