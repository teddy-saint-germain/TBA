# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1]
        if direction in ['nord','Nord','n','NORD','north']:
            direction='N'
        if direction in ['sud','Sud','s','SUD','south']:
            direction='S'
        if direction in ['est','Est','e','EST','east']:
            direction='E'
        if direction in ['ouest','Ouest','o','OUEST','west']:
            direction='O'
        if direction not in ['S','N','E','O']:
            print("\n cette direction n'existe pas!")
            print(game.player.current_room.get_long_description())
            return False
        # Move the player in the direction specified by the parameter.
        player.move(direction)
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    


    def up(game, list_of_words, number_of_parameters): 
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction =list_of_words[0]
        # Move the player in the direction specified by the parameter.
        player.move(direction)
        return True


    
    def down(game, list_of_words, number_of_parameters): 
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction =list_of_words[0]
        # Move the player in the direction specified by the parameter.
        player.move(direction)
        return True
    

    def back(game, list_of_words, number_of_parameters): 
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

    
        
        # Move the player in the direction specified by the parameter.
    
        
        if player.historic[-1] is None:
            print("\n vous ne pouvez pas revenir en arrière !\n")
            return False
        
        player.current_room = player.historic[-1]
        player.historic.pop()
        player.historic_name.pop()
        # Set the current room to the next room.
        print(player.current_room.get_long_description())
        return True
    

    def inventaire(game,list_of_words,number_of_parameters):
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        if player.inventary=={}:
            print("\n votre inventaire est vide !\n")
            return False
        
        print("\nVoici votre inventaire:")
        for obj in player.inventary_name:
            print("\t- " + str(obj))
        print()
        return True
    
    def look(game,list_of_words,number_of_parameters):
        player=game.player
        room =player.current_room
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        if room.inventary !={}:
            print("\non voit:")
            for obj in room.inventary.values():
                print(str(obj))
            print()

            if room.pnj!={}:
                print("\net il y a:")
                for obj in room.pnj.values():
                    print(str(obj))
                print()     
            else:       
                print("\n il n y a personne")
                return False
        
        else:

            if room.pnj!={}:
                print("\net il y a:")
                for obj in room.pnj.values():
                    print(str(obj))
                print()     
            else:       
                print("\n il n y a pas d'objet et il y a personne")
                return False
        return True
            
          
    
    def take(game, list_of_words, number_of_parameters): 
        player = game.player
        room= game.player.current_room
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

    
    
        
        if room.inventary =={}:
            print("\n il n'y a rien !\n")
            return False
        
        item = list_of_words[1]
        if item not in room.inventary.keys():
            print("\n cette objets n'est pas dans cette piece!\n")
            return False


        player.get_inventary(game,item)
        room.inventary.pop(f"{item}")
        
        return True
    


    def drop(game, list_of_words, number_of_parameters): 
        player = game.player
        room= game.player.current_room
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

    
    
        
        if player.inventary =={}:
            print("\n il n'y a rien dans votre inventaire !\n")
            return False
        
        item = list_of_words[1]
        if item not in player.inventary.keys():
            print("\n cette objets n'est pas dans votre inventaire!\n")
            return False


        room.get_inventary(game,item)
        player.inventary.pop(f"{item}")
        player.inventary_name.pop(f'{item.name}')
        
        return True
    

    def historic(game, list_of_words, number_of_parameters): 
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

    
        
        # Move the player in the direction specified by the parameter.
    
        
        if player.historic_name==[]:
            print("\n il n'y a pas d historique !\n")
            return False
        print("vous êtes deja aller dans ces endroit:")
        for sal in player.historic_name:
            print("\t- " + str(sal))
        print()
        
    
        
        return True
    



    