# Define the Player class.


class Player():

    # Define the constructor.
    def __init__(self, name,age):
        self.name = name
        self.age=age
        self.current_room = None 
        self.historic=[None]
        self.historic_name=[]
        self.inventary_name=[]
        self.inventary={}
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]
        
        
        #historic des room
        
        self.historic.append(self.current_room)
        self.historic_name.append(self.current_room.name)
        print("vous êtes deja aller dans ces endroit:")
        for sal in self.historic_name:
            print("\t- " + str(sal))
        print()

        #affichage historic
        
        

        self.current_room = next_room

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        print(self.current_room.get_long_description())
        return True
    

    def get_inventary(self,game,item):
        objet=game.items[item]

        self.inventary_name.append(objet.name)
        self.inventary[f'{item}']=objet
        print(f"\n vous avez ramasser,{objet.name}!\n")

        return True


    

    


    

    

    