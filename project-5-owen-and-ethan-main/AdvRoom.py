# File: AdvRoom.py

"""This module is responsible for modeling a single room in Adventure."""

#########################################################################
# Your job in this assignment is to fill in the definitions of the      #
# methods listed in this file, along with any helper methods you need.  #
# The public methods shown in this file are the ones you need for       #
# Milestone #1.  You will need to add other public methods for later    #
# milestones, as described in the handout.                              #
#########################################################################

# Constants

MARKER = "-----"

class AdvRoom:

    def __init__(self, name, shortdesc, longdesc, passages):
        """Creates a new room with the specified attributes.
        
        Args:
            name (str): the unique name of the room
            shortdesc (str): a short description of the room
            longdesc (list[str]): a list of strings making up a longer description
            passages (dict[str:str]): a dictionary of possible directions and
                corresponding room names
        Returns:
            None
        """
        self._name = name
        self._shortdesc = shortdesc
        self._longdesc = longdesc
        self._passages = passages
        self._visited = False
        self._objects = []

    def get_name(self):
        """Returns the name of this room."""
        return self._name

    def get_short_description(self):
        """Returns a one-line short description of this room.."""
        return self._shortdesc

    def get_long_description(self):
        """Returns the list of lines describing this room."""
        return self._longdesc

    def get_passages(self):
        """Returns the dictionary mapping directions to names."""
        return self._passages

    def set_visited(self, boolean):
        """Changes the visited boolean"""
        self._visited = boolean

    def has_been_visited(self):
        """Returns visited attribute"""
        return self._visited

    def add_object(self, object_name):
        """Adds object name to set of object names contained in the room."""
        self._objects.append(object_name)

    def remove_object(self, object_name):
        """Removes object name from set of object names contained in the room."""
        self._objects.remove(object_name)

    def contains_object(self, object_name):
        """Returns a boolean based on if object name is within the set of object names contained in the room."""
        if object_name in self._objects:
            return True
        return False

    def get_contents(self):
        """Returns a copy of the set of object names contained in the room."""
        return self._objects


# Method to read a room from a file

def read_room(f):
    """Reads the next room from the file, returning None at the end.

    Args:
        f (file handle): the file handle of the text file being read
    Returns:
        (AdvRoom or None): either an AdvRoom object or None if at end of file
    """
    name = f.readline().rstrip()             # Read the question name
    if name == "":                           # Returning None at the end
        return None

    shortdesc = [ ]
    sline = f.readline().rstrip()
    shortdesc.append(sline)

    longdesc = [ ]                               # Read the question text
    finished = False
    while not finished:
        line = f.readline().rstrip()
        if line == MARKER:
            finished = True
        else:
            longdesc.append(line)

    passages = {}                           # Read the answer dictionary
    finished = False
    while not finished:
        line = f.readline().rstrip()
        if line == "":
            finished = True
        else:
            colon = line.find(":")
            if colon == -1:
                raise ValueError("Missing colon in " + line)
            response = line[:colon].strip().upper()
            next_room= line[colon + 1:].strip()
            passages[response] = next_room

    return AdvRoom(name, shortdesc, longdesc, passages)  # Return the completed object
