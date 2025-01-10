
class Event:
    def __init__(self, name, desc=None, date=None, location=None):
        self.name = name
        self.description = desc
        self.date = date
        self.location = location

    def set_desc(self, desc):
        self.description = desc

    def set_date(self, date):
        self.date = date
    
    def set_location(self, location):
        self.location = location