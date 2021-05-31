from room import Room
from character import Enemy, Friend
from item import Item

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

# create characters
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Grrr Arrgh!")
dave.set_weakness("Cheese")

chelsea = Friend("Chelsea", "A nervous squirel")
chelsea.set_conversation("Eeek! Shadows")

# add character to rooms
dining_hall.set_character(dave)
ballroom.set_character(chelsea)

# create items
cheese = Item("Cheese")
cheese.set_description("super smelly")

chair = Item("Chair")
chair.set_description("designed to be sat on")

elmo = Item("Elmo")
elmo.set_description("wanting to be tickled")

# add items to rooms
kitchen.set_item(elmo)
dining_hall.set_item(chair)
ballroom.set_item(cheese)

#describe the rooms
#kitchen.describe()
#dining_hall.describe()
#ballroom.describe()

# intialise the variables
running = True
current_room = kitchen
backpack = []

# ----- MAIN LOOP -----
while running:
    inhabitant = current_room.get_character()
    current_room.describe()
        
    command = input("> ").lower()
    
    # move
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    # talk
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There is no one here to talk to")
    # fight
    elif command == "fight":
        if inhabitant is not None:
            weapon = input("What will you fight with? > ").lower()
            if weapon in backpack:
                if inhabitant.fight(weapon):
                    current_room.set_character(None)
                else:
                    running = False
            else:
                print(f"You don't have {weapon}")
                print(f"{inhabitant.get_name()} strikes you down as you rummage through your backpack")
                running = False
        else:
            print("There is no one here to fight")
    # hug
    elif command == "hug":
        if inhabitant is not None:
            inhabitant.hug()
        else:
            print("There is no one here to hug")
    # take
    elif command == "take":
        if current_room.get_item() != None:
            backpack.append(current_room.get_item().get_name())
            print(f"You take {current_room.get_item().get_name()}")
            current_room.set_item(None)
        else:
            print("There is nothing here to take")
    # backpack
    elif command == "backpack":
        if backpack == []:
            print("You have nothing")
        else:
            print("You have:")
            for item in backpack:
                print(item.capitalize())
    elif command == "quit":
        running = False
