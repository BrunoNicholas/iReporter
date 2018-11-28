import datetime

class Intervention:
    ''' this is the model class for the interventions '''
    counter = 0

    def __init__(self, title, description, latitude, longitude, attachement, status):
        self.id = Intervention.counter + 1
        self.title = title
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.attachement = attachement
        self.status = status
        self.created_at = str(datetime.datetime.now())[:10]
