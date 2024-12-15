# Description: Game class

# Import modules
from character import Character
from Item import Item
from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.items={}
        self.room=None
        self.characters={}
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        up=Command("up"," : monter à l'étage",Actions.up,0)
        self.commands["up"]=up
        down=Command("down"," :descendre ",Actions.down,0)
        self.commands["down"]=down
        back=Command("back"," revenir en arrière",Actions.back,0)
        self.commands["back"]=back
        inventaire=Command('inventaire',' affiche ton inventaire',Actions.inventaire,0)
        self.commands['inventaire']=inventaire
        look=Command('look',' montre les objets dans la piece ',Actions.look,0)
        self.commands['look']=look
        take=Command('take',' rammaser un objets',Actions.take,1)
        self.commands['take']=take
        drop=Command('drop',' depose l objet au sol',Actions.drop,1)
        self.commands['drop']=drop
        historic=Command('historic',' afficher l historic',Actions.historic,0)
        self.commands['historic']=historic
        
        
        # Setup rooms

        forest = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(forest)
        tower = Room("Tower", "dans une immense tour en pierre qui s'élève au dessus des nuages.")
        self.rooms.append(tower)
        cave = Room("Cave", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
        self.rooms.append(cave)
        cottage = Room("Cottage", "dans un petit chalet pittoresque avec un toit de chaume. Une épaisse fumée verte sort de la cheminée.")
        self.rooms.append(cottage)
        swamp = Room("Swamp", "dans un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
        self.rooms.append(swamp)
        castle = Room("Castle", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(castle)
        couloir= Room("couloir","vous êtes dans un couloir avec un escalier qui monte et un autre qui descend")
        self.rooms.append(couloir)
        donjon= Room("donjon","vous arrivez dans un donjon, il n'y a rien")
        self.rooms.append(donjon)
        

        # Create exits for rooms

        forest.exits = {"N" : cave, "E" : None, "S" : castle, "O" : None , "up": None ,"down": None}
        tower.exits = {"N" : cottage, "E" : None, "S" : None, "O" : None, "up": None ,"down": couloir}
        cave.exits = {"N" : None, "E" : cottage, "S" : forest, "O" : None ,"up": None ,"down": None}
        cottage.exits = {"N" : None, "E" : None, "S" : tower, "O" : cave ,"up": None ,"down": None}
        swamp.exits = {"N" : tower, "E" : None, "S" : None, "O" : castle, "up": None ,"down": None}
        castle.exits = {"N" : forest, "E" : couloir, "S" : None, "O" : None, "up": None ,"down": None}
        couloir.exits ={"N": None, "E": cave, "S": castle, "O": None ,"up": tower ,"down": donjon}
        donjon.exits={"N": None, "E": None, "S": None, "O": None ,"up": couloir ,"down": None}

        # setup Items
        key=Item("clé","tu une cle sur le sol",2)
        self.items['key']=key

        #setup pnj
        kenny=Character('kenny','un gars chill',['salut','ca va'])
        self.characters['kenny']=kenny
        

        #setup emplacements
        couloir.inventary={'key':key}
        couloir.pnj={'kenny':kenny}
 

        # Setup player and starting room

        self.player= Player(input("\nEntrez votre nom: "),int(input("\nEntrez votre age: ")))

        if self.player.age<16:
            command = self.commands["quit"]
            command.action(self,['quit'],0)

        self.player.current_room = couloir

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:


        # Split the command string into a list of words
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]

        #loop si on fait entrer
        if command_word =='':
            while not self.finished:
                # Get the command from the player
                self.process_command(input("> "))
            return None
        
        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        if self.player.age<16:
            print(f"\n{self.player.name} quitte le jeu!!, ce jeu est interdit au mois de 16 ans!!!")
        else:
            print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
            print("Entrez 'help' si vous avez besoin d'aide.")
            print(self.player.current_room.get_long_description())
    
def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
