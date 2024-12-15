import random

class Character():

    def __init__(self,name,description,msg):
        self.name=name
        self.description=description
        self.current_room=None
        self.msg=msg
        self.next_room=None


    def __str__(self):
        return f"\n \t- {self.name} : {self.description}"
    

    def move(self,game):
        self.next_room=random.choice(game.rooms)
        if self.current_room== self.current_room:
            return False
        self.current_room=self.next_room
        return True
