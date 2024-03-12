# File: AdvGame.py

"""
This module defines the AdvGame class, which records the information
necessary to play a game.
"""

###########################################################################
# Your job in this assignment is to fill in the definitions of the        #
# methods listed in this file, along with any helper methods you need.    #
# Unless you are implementing extensions, you won't need to add new       #
# public methods (i.e., methods called from other modules), but the       #
# amount of code you need to add is large enough that decomposing it      #
# into helper methods will be essential.                                  #
###########################################################################

from AdvRoom import AdvRoom, read_room
from AdvObject import AdvObject, read_object
from tokenscanner import TokenScanner   

class AdvGame:

    def __init__(self, prefix):
        """Reads the game data from files with the specified prefix.
        Args:
            prefix (str): The prefix starting each of the file names
        Returns:
            None
        """
        self._prefix = prefix

        self._rooms = { }
        self._objects = { }
        self._inventory = [ ]

        rooms_filename = prefix + "Rooms.txt"
        with open(rooms_filename) as f:
            finished = False
            while not finished:
                rooms = read_room(f)
                if rooms is None:
                    finished = True
                else:
                    name = rooms.get_name()
                    if len(self._rooms) == 0:
                        self._rooms["START"] = rooms
                    self._rooms[name] = rooms

        objects_filename = prefix + "Objects.txt"
        with open(objects_filename) as f:
            finished = False
            while not finished:
                objects = read_object(f)
                if objects is None:
                    finished = True
                
                else:
                    name = objects.get_name()
                    self._objects[name] = objects

        for i in self._objects:
            loc = self._objects[i].get_initial_location()
            if loc != "PLAYER":
                self._rooms[loc].add_object(i)
            else: 
                self._inventory.append(self._objects[i])

    def get_room(self, name):
        """Returns the AdvRoom object with the specified name.
        Args:
            name (str): the unique name of a room
        Returns:
            (AdvRoom): the corresponding AdvRoom object
        """
        return self._rooms[name]

    def take_object(self, object_name, room):###########
        print("hello")
        room.remove_object(object_name)
        self._inventory.append(object_name)

    def drop_object(self, object_name, room):###########
        self._inventory.remove(object_name)
        room.add_object(object_name)

    def run(self):
        """Plays the adventure game stored in this object."""
        current = "START"
        room_text = True
        help_text = False
        inventory_text = False
        take_text = False ###########
        drop_text = False ###########

        while current != "EXIT":
            room = self.get_room(current)
            if room_text:
                if not room.has_been_visited():
                    for line in room.get_long_description():
                        print(line)
                    object_list = room.get_contents()
                    for name in object_list:
                        objects = self._objects[name]
                        if objects is not None:
                            print("There is " + objects.get_description() + " here.")
                else: 
                    for line in room.get_short_description():
                        print(line)
            else:
                if help_text:
                    for line in HELP_TEXT:
                        print(line)
                    help_text = False

                if inventory_text:
                    if len(self._inventory) > 0:
                        print("You are carrying:")
                        for obj in self._inventory:
                            description = obj.get_description()
                            print(f"  {description}")
                    else:
                        print("You are empty-handed")
                    inventory_text = False

            room_text = True
            room.set_visited(True)
            response = input("> ").upper()
            first = get_word(response, 0) ###########
            second = get_word(response, 2) ###########
            print(first)
            print(second)
            passages = room.get_passages()
            if is_action(first):
                if response == "LOOK":
                    room.set_visited(False)

                elif response == "QUIT":
                    current = "EXIT"

                elif response == "HELP":  
                    room_text = False
                    help_text = True

                elif response == "INVENTORY":
                    room_text = False
                    inventory_text = True

                elif first == "TAKE": ###########
                    if room.contains_object(second):
                        self.take_object(second, room)
                        room_text = False
                        take_text = True

                elif first == "DROP": ###########
                    room_text = False
                    drop_text = True

            #else:
            next_room = passages.get(response, None)
            if next_room is None:
                next_room = passages.get("*", None)
            if next_room is None:
                print("I don't understand that response.")
            elif current != "EXIT":
                current = next_room


def is_action(word):
    actions = ["QUIT","HELP","LOOK","INVENTORY","TAKE","DROP"]
    if word in actions:
        return True
    else: 
        return False

def get_word(input, index):
    """Helper function to return the word at the specified index from input string"""
    scanner = TokenScanner()
    scanner.set_input(input)
    words = []
    while scanner.has_more_tokens():
        token = scanner.next_token()
        words.append(token)
    if len(words) > index:
        return words[index]
    print(words)



# Constants

HELP_TEXT = [
    "Welcome to Adventure!",
    "Somewhere nearby is Colossal Cave, where others have found fortunes in",
    "treasure and gold, though it is rumored that some who enter are never",
    "seen again.  Magic is said to work in the cave.  I will be your eyes",
    "and hands.  Direct me with natural English commands; I don't understand",
    "all of the English language, but I do a pretty good job.",
    "",
    "It's important to remember that cave passages turn a lot, and that",
    "leaving a room to the north does not guarantee entering the next from",
    "the south, although it often works out that way.  You'd best make",
    "yourself a map as you go along.",
    "",
    "Much of my vocabulary describes places and is used to move you there.",
    "To move, try words like IN, OUT, EAST, WEST, NORTH, SOUTH, UP, or DOWN.",
    "I also know about a number of objects hidden within the cave which you",
    "can TAKE or DROP.  To see what objects you're carrying, say INVENTORY.",
    "To reprint the detailed description of where you are, say LOOK.  If you",
    "want to end your adventure, say QUIT."
]
