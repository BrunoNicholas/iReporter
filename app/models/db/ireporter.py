class UsersData:
    """ This list stands as the database table for the users """

    def __init__(self):
        self.users = []

    def table(self, values=None):
        if values:
            self.users.append(values)
        return self.users


class RedFlagsData:
    """ This list stands as the database table for the red flags """

    def __init__(self):
        self.redFlags = []

    def table(self, values=None):
        if values:
            self.redFlags.append(values)
        return self.redFlags


class InterventionsData:
    """ This list stands as the database table for the interventions """

    def __init__(self):
        self.interventions = []

    def table(self, values=None):
        if values:
            self.interventions.append(values)
        return self.interventions


class LocatorData:
    """ This list stands as the database table for the location coordinates on the map """

    def __init__(self):
        self.locations = []

    def table(self, values=None):
        if values:
            self.locations.append(values)
        return self.locations
