import datetime

START_OF_TIME = datetime.datetime(1970, 1, 1)

class TimeLine:
    def __init__(self, start=START_OF_TIME, end=datetime.datetime.now()):
        self.start = start
        self.end = end
        self.memories = []

    def add_memory(self, memory):
        self.meories.append(memory);

    def __str__(self):
        return f"Timeline (Starting: {self.start}, Ending: {self.end})"
