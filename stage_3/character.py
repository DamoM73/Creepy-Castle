class Character():
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def set_conversation(self, value):
        self.conversation = value
        
    def get_conversation(self):
        return self.conversation
    
    def describe(self):
        print(f"{self.name} is here. {self.description}")
        
    def talk(self):
        if self.conversation is not None:
            print(f"{self.name}: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you")