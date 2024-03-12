# File: EnigmaModel.py

""" This is the starter file for the Enigma project. """

from EnigmaView import EnigmaView
from EnigmaConstants import ROTOR_PERMUTATIONS, ALPHABET, REFLECTOR_PERMUTATION


class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation= permutation
        self.offset = 0

    def get_offset(self):
        return self.offset

    def get_permutation(self):
        return self.permutation
    
    def advance(self):
        self.offset += 1
        if self.offset == 26:
            self.offset = 0
            return True
        return False

def apply_permutation(index, permutation, offset):
    shifted = (index + offset) % 26
    target = ALPHABET.index(permutation[shifted])
    return (target - offset + 26) % 26   

def invert_key(key):
    new_key = ""
    for ch in ALPHABET:
        new_key += ALPHABET[key.find(ch)]
    return new_key

class EnigmaModel:
    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = []
        self._keys = {letter: False for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        self._lamp_states = {letter: False for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        self.rotors = [EnigmaRotor(i) for i in ROTOR_PERMUTATIONS]

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self._keys[letter]

    def is_lamp_on(self, letter):
        """Returns True if the lamp associated with the given letter is on, False otherwise."""
        return self._lamp_states[letter]

    def key_pressed(self, letter):
        """Updates the internal state of the model to record that a key has been pressed."""
        index= ALPHABET.index(letter)
        rotc = self.rotors[2].advance()
        if rotc:
            rotc = self.rotors[1].advance()
        if rotc:
            self.rotors[0].advance()

        for i in range(2,-1,-1):
            index= apply_permutation(index, ROTOR_PERMUTATIONS[i], self.rotors[i].get_offset())
        
        index= apply_permutation(index,REFLECTOR_PERMUTATION, 0)

        for j in range(3):
            index= apply_permutation(index, invert_key(ROTOR_PERMUTATIONS[j]), self.rotors[j].get_offset())

        self._lamp_states[ALPHABET[index]] = True
        self._keys[letter] = True
        self.update()

    def key_released(self, letter):
        """Updates the internal state of the model to record that a key has been released."""
        index= ALPHABET.index(letter)
        for i in range(2,-1,-1):
            index= apply_permutation(index, ROTOR_PERMUTATIONS[i], self.rotors[i].get_offset())
        
        index= apply_permutation(index,REFLECTOR_PERMUTATION, 0)

        for j in range(3):
            index= apply_permutation(index, invert_key(ROTOR_PERMUTATIONS[j]), self.rotors[j].get_offset())
        
        self._lamp_states[ALPHABET[index]] = False
        self._keys[letter] = False
        self.update()

    def get_rotor_letter(self, index):
        return ALPHABET[self.rotors[index].get_offset()]

    def rotor_clicked(self, index):
        # You need to fill in this code
        self.rotors[index].advance()
        self.update()




def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)


# Startup code

if __name__ == "__main__":
    enigma()





