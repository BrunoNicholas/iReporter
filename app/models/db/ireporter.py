class UsersData:
    """ This list stands as the database table for the users """

    def __init__(self):
        self.users = [
            {
                "user_id": 1,
                "name": "Bruno Nicholas",
                "email": "sbnibro256@gmail.com",
                "password": "xvg113h54?x!ncdiihn#jdfg",
                "telephone": "0782407042",
                "created_at": "18-01-2019 2:12:04"
            },
            {
                "user_id": 2,
                "name": "Catherine Coolman",
                "email": "cahy1910@gmail.com",
                "password": "5l4pzo?fx!bcfjkkxdsajfjd",
                "telephone": "07612407080",
                "created_at": "18-01-2019 2:30:14"
            }
        ]

    def table(self, values=None):
        if values:
            self.users.append(values)
        return self.users


class RedFlagsData:
    """ This list stands as the database table for the red flags """

    def __init__(self):
        self.redFlags = [
            {
                "red_id": 1,
                "title": "Stolen NAADS funds",
                "description": "There has been a theft incidence of solen funds in New Vision",
                "latitude": 15.112,
                "longitude": 3.442,
                "attachement": "snapshot_24.jpg",
                "status": "Under Investigation",
                "created_at": "18-01-2019 4:46:24"
            }
        ]

    def table(self, values=None):
        if values:
            self.redFlags.append(values)
        return self.redFlags


class InterventionsData:
    """ This list stands as the database table for the interventions """

    def __init__(self):
        self.interventions = [
            {
                "int_id": 1,
                "title": "Deadly potholes on road",
                "description": "There are some bad flooding roads in Bakuli",
                "latitude": 28.142,
                "longitude": 6.281,
                "attachement": "mov_13.mp4",
                "status": "Pending",
                "created_at": "18-01-2019 6:28:45"
            }
        ]

    def table(self, values=None):
        if values:
            self.interventions.append(values) 
        return self.interventions 
