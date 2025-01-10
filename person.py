
class Person:
    def __init__(self, name, locations=[], memories=[]):
        self.name = name
        self.locations = locations
        self.memories = memories

    def add_location(self, location):
        self.locations.append(location)

    def add_memory(self, memory):
        self.memories.append(memory)
