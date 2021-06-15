from helpers import *
#############################################
#    Defines Rotor class that represents    #
#    the different rotors that can be used  #
#    in the enigma machine                  #
#############################################
TURNOVERS = {"ROTOR I": "Q", "Rotor II":"E", "Rotor III":"V"} #Specifies the turnover points that kick the next rotor
class Rotor:
    def __init__(self, name, encoding, offset):
        """
        Creates an instance of Rotor
        """
        self.name = name
        self.writingSpec = encoding
        self.offset = offset
        self.turnover = TURNOVERS[name]
    
    def map_r_to_l(self, c):
        """
        Represents current flowing from right to left in the rotor
        """
        c = c.upper()
        i = (index(c) + self.offset)  
        encoded = self.writingSpec[i] #encoded version of c according to the wiring specification of the rotor
        # encoded_index = index(encoded) #index in alphabet of encoding of c
        print("Encoding from R to L " + c + " becomes " + encoded)
        return encoded

    def map_l_to_r(self, c):
        """
        Represents current flowing from left to right in the rotor, returns encoding of c 
        """
        c = c.upper()
        c_index = index(c)
        c_index += self.offset #add offset to the input contact
        c_offset_char = chr(c_index+65) 
        encoded_index = self.inverse_index(c_offset_char) #index in alphabet of encoding of c
        encoded = chr(encoded_index+65)
        print("Encoding from L to R " + c + " becomes " + encoded)
        return encoded
        
    def set_offset(self, offset):
        """
        Allows user to set the top letter (starting position/offset) of the rotor
        """
        if not offset.numeric():
            raise Exception("Offest must be a number between 0 and 25")
        elif offset > 25:
            raise Exception("Offest must be a number between 0 and 25")
        
        self.offset = offset

    def get_offset(self):
        """
        Return the current offset of the rotor
        """
        return self.offset

    def get_writingSpec(self):
        return self.writingSpec


    def inverse_index(self, c):
        """
        Return the index of c in the writingSpec of the rotor
        """
        return self.writingSpec.index(c)

    def __eq__(self, other):
        if self.writingSpec == other.writingSpec:
            return True
        return False