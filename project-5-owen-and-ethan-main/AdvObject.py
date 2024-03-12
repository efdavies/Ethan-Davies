# File: AdvObject.py

"""This module defines a class that models an object in Adventure."""

#########################################################################
# Your job in this assignment is to fill in the definitions of the      #
# methods listed in this file, along with any helper methods you need.  #
# You won't need to work with this file until Milestone #4.  In my      #
# solution, none of the milestones required any public methods beyond   #
# the ones defined in this starter file.                                #
#########################################################################

class AdvObject:

    def __init__(self, name, description, location):
        """Creates an AdvObject from the specified properties.

        Args:
            name (str): the unique name of the object
            description (str): a short description of the object
            location (str): the name of the location where the object first appears
        """
        self._name = name
        self._description = description
        self._location = location

    def __str__(self):
        """Converts an AdvObject to a string."""
        return f"AdvObject({self._name}, {self._description}, {self._location})"

    def get_name(self):
        """Returns the name of this object."""
        return self._name

    def get_description(self):
        """Returns the description of this object."""
        return self._description

    def get_initial_location(self):
        """Returns the initial location of this object."""
        return self._location

# Method to read an object from a file

def read_object(f):
    """Reads the next object from the file, returning None at the end.

    Args:
        f (file handle): the file handle of the opened objects text file
    Returns:
        (AdvObject or None): an AdvObject object or None if at end of the file
    """
    name = f.readline().rstrip()
    if name == "":
        return None
    description = f.readline().rstrip()
    location = f.readline().rstrip()
    f.readline().rstrip()

    return AdvObject(name, description, location)