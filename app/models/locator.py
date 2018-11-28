
class GeoLocator:
    ''' this id the model class for the '''
    counter = 0

    def __init__(self, latitude,longitude,location=None):
        self.id = GeoLocator.counter + 1
        self.latitude = latitude
        self.longitude = longitude
        self.location = location
        