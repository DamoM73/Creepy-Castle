class Room():
    
    def __init__(self, room_name):
        # initalises the room object
        self.name = room_name.lower()
        self.description = None
        self.linked_rooms = {}

    def set_description(self,value):
        # sets the description to the provided string
        self.description = value
        
    def get_name(self):
        return self.name

    def set_linked_rooms(self, room_to_link, direction):
        # links the provided room, in the provided direction
        self.linked_rooms[direction] = room_to_link

    def describe(self):
        # prints the details of the room to the display
        print(f"\nYou are in the {self.name}:")
        print(self.description)
        for direction in self.linked_rooms:
            print(f"To the {direction} is the {self.linked_rooms[direction].get_name()}")
        
