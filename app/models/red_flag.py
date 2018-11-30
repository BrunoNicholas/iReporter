import datetime


class RedFlag:
    """ the model for working with the Red Flags """
    counter = 0

    def __init__(self, title, description, latitude, longitude, attachement, status):
        self.red_id = RedFlag.counter + 1
        self.title = title
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.attachement = attachement
        self.status = status
        self.created_at = str(datetime.datetime.now())[:10]
