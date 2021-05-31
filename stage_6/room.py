class Room():
    
    def __init__(self, room_name):
        # initalises the room object
        self.name = room_name.lower()
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_description(self,value):
        # sets the description to the provided string
        self.description = value
        
    def get_name(self):
        return self.name

    def set_linked_rooms(self, room_to_link, direction):
        # links the provided room, in the provided direction
        self.linked_rooms[direction] = room_to_link

    def set_character(self,character):
        self.character = character
        
    def get_character(self):
        return self.character
    
    def set_item(self,item):
        self.item = item
        
    def get_item(self):
        return self.item

    def describe(self):
        # prints the details of the room to the display
        print(f"\nYou are in the {self.name}:")
        print(self.description)
        if self.character is not None:
            print(f"{self.character.get_name()} is here. {self.character.get_description()}")
        if self.item is not None:
            self.item.describe()
        for direction in self.linked_rooms:
            print(f"To the {direction} is the {self.linked_rooms[direction].get_name()}")
        
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
        
    