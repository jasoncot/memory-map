from timeline import TimeLine
from memory import Memory

class User:
    def __init__(self, name):
        self.name = name
        self.timeline = TimeLine()
        self.memories = []
        self.people = []
        self.locations = []

    def add_memory(self, memory):
        self.memories.append(memory)

    def add_person(self, person):
        self.people.append(person)
    
    def add_location(self, location):
        self.locations.append(location)

    def set_timeline(self, timeline):
        self.timeline = timeline

    def create_memory(self, desc, date=None, location=None, people=None):
        new_memory = Memory.of(desc)
        if date != None:
            new_memory.set_date(date)
        if location != None:
            new_memory.set_location(location)
        if people != None:
            if isinstance(people, list):
                for person in people:
                    new_memory.add_person(person)
            else:
                new_memory.add_person(people)
        self.add_memory(new_memory)
        return new_memory

    def __str__(self):
        return f"User: {self.name}, Timeline: {self.timeline}, Memories: {self.memories}"