import datetime

from db.ireportter import UserData

class User:
    ''' This id the model class for the user or users '''
    counter = 0

    def __init__(self, name, email, password, telephone=None):
        self.id = User.counter + 1
        self.name = name
        self.email = email
        self.password = password
        self.telephone = telephone
        self.created_at = str(datetime.datetime.now())[:10]
