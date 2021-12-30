import json
import datetime
import time

'''
event = {
        "name": "event1",
        "description": "quick zoom with the module coordinator",
        "week": "Week 4",
        "date": "date example",
        "module": "CT2002",
        "due" : "example date"
    }
'''

def main():

    while True:

        print("===========================")
        print("Garbhan's NUIG Planner App")
        print("What would you like to do?...\n")

        print("Press (1) to add an event...")
        print("Press (2) to remove an event...")
        print("Press (3) to view timetable...")
        print("Press (4) to view events...")
        print("Press (5) to exit")

        do = input()

        match do:
            case "1":
                print("add event")
                event = {}

                event_name = input("Event name: ")
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
                    print(f"({len(data)+1}) Quit to main menu")
                    
                    # take index as input, then loop over data and delete entry with matching key
                    to_delete = input("\nWhich event do you want to remove?... \n")
                    if to_delete == len(data)+1:
                        continue
                    #print(f"deleting {to_delete}...\n")

                for i, entry in enumerate(data.copy()):
                    if i+1 == int(to_delete):
                        data.pop(entry)
                        print(f"{entry} has been removed\n")
                    else:
                        "Sorry, no entry for that index."
                
                with open("plans.json", "w") as file:
                    data = json.dump(data, file, indent=4)
                continue

            # View Timetable    
            case "3":
                print("view timeable coming soon!\n")
                time.sleep(1)
                continue

            
            # View all saved Events, loaded from local JSON
            case "4":
                with open("plans.json", "r") as file:
                    data = json.load(file)
                    for key in data.keys():
                        print(f"-------- {key} --------\n")
                        for key, val in data[key].items():
                            print(f"{key}: {val}")
                        print("\n")
                continue
            
            case "5":
                print("""\

                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ.   cya
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /


                    """)
                quit()

if __name__ == "__main__":
    main()