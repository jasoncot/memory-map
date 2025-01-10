
class Location:
    def __init__(self, name, address=None, date_or_range=None):
        self.name = name
        self.address = address
        self.date_or_range = date_or_range

    def add_address(self, address):
        self.address = address

    def add_date(self, date):
        self.date_or_range = date