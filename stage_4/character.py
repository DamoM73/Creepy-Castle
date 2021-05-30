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
            
    def fight(self, item):
        print(f"{self.name} doesn't want to fight you")
        return True
    
    def hug(self):
        print(f"{self.name} doesn't want to hug you")
        

class Friend(Character):
    def __init__(self,name,description):
        super().__init__(name,description)
        
    def hug(self):
        print(f"{self.name} squeels and hugs you back!")


class Enemy(Character):
    def __init__(self,name, description):
        super().__init__(name, description)      
        self.weakness = None
        
    def set_weakness(self,item):
        self.weakness = item.lower()
        
    def get_weakness(self):
        return self.weakness
    
    def fight(self, item):
        if item == self.weakness:
            print(f"You strike {self.name} down with {item}")
            return True
        else:
            print(f"{self.name} crushes you. Puny adventurer")
            return False