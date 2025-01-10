
class Memory:
    def __init__(self, desc, time_or_range=None, location=None, ppl=[]):
        self.description = desc
        self.time_or_range = time_or_range
        self.location = location
        self.people = ppl

    def add_person(self, person):
        self.people.append(person)
    
    def set_location(self, location):
        self.location = location

    def set_description(self, description):
        self.description = description
    
    def set_date(self, date):
        self.time_or_range = date

    def of(desc):
        return Memory(desc)