class Item():
    def __init__(self, name):
        self.name = name.lower()
        self.description = None
        
    def get_name(self):
        return self.name

    def set_description(self,description):
        self.description = description
        
    def get_deccription(self):
        return self.description
        
    def describe(self):
        print(f"You see {self.name} in the room. It is {self.description}.")