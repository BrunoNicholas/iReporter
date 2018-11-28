# interventions = {}

class UsersData:
    """ This dictionary stands as the database table for the users """
    def __init__(self):
        self.users = []
        
    def connect (self):
        return self.users

    # def read (self, id):
    #     try:
    #         if id is None:
    #             self.connect()
    #         else:
    #             return (jsonify(self.users[f'{id}']))
    

class RedFlagsData:
    """ This dictionary stands as the database table for the red flags """
    def __init__(self):
        self.redFlags = []

    def connect(self):
        return self.redFlags
        

class InterventionsData:
    """ This dictionary stands as the database table for the interventions """
    def __init__(self):
        self.interventions = []

    def connect(self):
        return self.interventions


class LocatorData:
    def __init__(self):
        self.locations = []

    def connect(self):
        return self.locations
        
