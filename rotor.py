
#############################################
#    Defines Rotor class that represents    #
#    the different rotors that can be used  #
#    in the enigma machine                  #
#############################################

class Rotor:
    #TODO: Insert params and attributes
    def __init__(self, encoding, offset):
        """
        Creates an instance of Rotor
        """
        self.writingSpec = encoding
        self.offset = offset
    
    #TODO: Insert params
    def map_r_to_l(self):
        """
        Represents current flowing from right to left in the rotor
        """
    
    #TODO: Insert params
    def map_l_to_r(self, c):
        """
        Represents current flowing from left to right in the rotor, returns encoding of c 
        """
        i = self.index(c)
        

    #TODO: Insert params
    def set_offset(self, offset):
        """
        Allows user to set the top letter (starting position/offset) of the rotor
        """
        self.offset = offset

    def get_offset(self):
        """
        Return the current offset of the rotor
        """
        return self.offset

    def index(self, c):
        """
        Return the index in the alphabet of c
        """
        return ord(c) - 97