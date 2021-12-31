import json
import datetime

'''
sample event = {
        "name": "event1",
        "description": "quick zoom meeting with the module coordinator",
        "week": "4",
        "module": "CT2002",
        "due" : "Wed 16 March 2022"
    }
'''

class bcolors:
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PINK = '\033[95m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'

def main():
    while True:
        print("===========================")
        print(f"{bcolors.YELLOW}Garbhan's NUIG Planner App{bcolors.ENDC}")
        print("What would you like to do?...\n")

        print("Press (1) to add an event...")
        print("Press (2) to remove an event...")
        print("Press (3) to view timetable...")
        print("Press (4) to view events...")
        print("Press (5) to exit")

        do = input()

        match do:
            # Add a new event
            case "1":
                event = {}

                event_name = input(f"{bcolors.PINK}Event name: {bcolors.ENDC}")
                event["name"] = event_name

                event_desc = input("Event description: ")
                event["description"] = event_desc

                event_week = input("Week: ")
                event["week"] = event_week

                event_module = input("Select module: ")
                event["module"] = event_module

                event_due = input("Due date (YYYY/M/D): ")
                dates = event_due.split('/')
                event_due = datetime.datetime(int(dates[0]), int(dates[1]), int(dates[2]))
                event_due = event_due.strftime("%a %d %B %Y")
                event["due"] = event_due

                # add the dict to a parent dict so it has a key in the json file
                events_parent = {}
                events_parent.update({event["name"]: event})

                # Add it to the events.json file
                with open("plans.json", "r+") as file:
                    data = json.load(file)
                    data.update(events_parent)
                    file.seek(0)
                    json.dump(data, file, indent=4)
                print(f'\n {event["name"]} has been added!\n')
                continue

            # Remove an Event from local JSON
            case "2":
                with open("plans.json", "r") as file:
                    data = json.load(file)
                    # loop over entries with an index, entry name and description
                    # may change from description to something else later            
                    for i, entry in enumerate(data):
                        print(f"\n({i+1}) {entry}: {data[entry]['description']}")
                    print(f"\n({len(data)+1}) Quit to main menu")

                    # take index as input, then loop over data and delete entry with matching key
                    to_delete = input("\nWhich event do you want to remove?... \n")
                    if to_delete == len(data)+1:
                        continue

                for i, entry in enumerate(data.copy()):
                    if i+1 == int(to_delete):
                        data.pop(entry)
                        print(f"{bcolors.RED}{entry} has been removed{bcolors.ENDC}\n")
                    else:
                        "Sorry, no entry for that index."

                with open("plans.json", "w") as file:
                    data = json.dump(data, file, indent=4)
                continue

            # View Timetable    
            case "3":
                print('''
                | Time | Monday        | Tuesday       | Wednesday | Thursday     |
                | ---- | ------------- | ------------- | --------- | ------------ |
                | 9am  |               | Lab - DSwR    |           | Lab - BI     |
                | 10am | Lec - DSwR    | Lab - DSwR    | Lec - BI  | Lab - BI     |
                | 11am | Lec - DSwR    | Lec - Stats2  | Lec - BI  | Lec - Stats2 |
                | 12pm |               |               |           |              |
                | 1pm  |               | Lec - DataVis |           |              |
                | 2pm  | Lec - DataVis | TBD           |           |              |
                | 3pm  | Lec - DataVis |               |           |              |
                | 4pm  | Lec - Stats   |               |           |              |
                | 5pm  |               |               |           |              |
                | 6pm  |               |               |           |              |

                ''')
                continue

            # View all saved Events, loaded from local JSON
            case "4":
                with open("plans.json", "r") as file:
                    data = json.load(file)
                    for key in data.keys():
                        print(f"{bcolors.GREEN}-------- {key} --------{bcolors.ENDC}\n")
                        for key, val in data[key].items():
                            print(f"{key}: {val}")
                        print("\n")
                continue

            # exit the application
            case "5":
                print("""
                       ___  
                      /  .\ 
                     /  =__|
                cya /    ||

                    """)
                quit()

if __name__ == "__main__":
    main()
