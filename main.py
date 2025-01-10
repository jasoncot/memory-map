import datetime
from timeline import TimeLine
from user import User
from memory import Memory

ADD_MEMORY = 'add_memory'
ADD_EVENT = 'add_event'
def show_options(user):
    print(f"These are your available options")
    print(f"1. add a memory")
    print(f"2. list memories")
    print(f"3. remove a memory")
    print(f"4. add an event")
    print(f"5. list events")
    print(f"6. remove an event")
    print(f"7. view timeline")

def get_user_option(user):
    return input()

def perform_action(user, input):
    if input == ADD_MEMORY:
        # get user input here


def main():
    print("Please enter your name:")
    name = input()
    user = User(name)

    print("What year would you like the timeline to start? (e.g. 1980)")
    starting_year = int(input(), 10)

    print("What year would you like the timeline to end? (empty for now)")
    end_input = input()

    timeline = None
    if end_input == '':
        timeline = TimeLine(datetime.datetime(starting_year, 1, 1))
    else:
        timeline = TimeLine(starting_year, int(end_input, 10))

    user.set_timeline(timeline)

    print(user)

main()