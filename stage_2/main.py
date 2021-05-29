from room import Room

# create rooms
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty place, buzzing with flies")

dining_hall = Room("Dining hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesitcks guard the entrance")

# link rooms
kitchen.set_linked_rooms(dining_hall,"south")
dining_hall.set_linked_rooms(kitchen,"north")
dining_hall.set_linked_rooms(ballroom,"west")
ballroom.set_linked_rooms(dining_hall,"east")

# describe the rooms
#kitchen.describe()
#dining_hall.describe()
#ballroom.describe()

# intialise the variables
running = True
current_room = kitchen

# ----- MAIN LOOP -----
while running:
    current_room.describe()
    
    command = input("> ").lower()
    
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "quit":
        running = False