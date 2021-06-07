from helpers import *
#############################################
#    Defines Rotor class that represents    #
#    the different rotors that can be used  #
#    in the enigma machine                  #
#############################################

class Rotor:
    def __init__(self, encoding, offset):
        """
        Creates an instance of Rotor
        """
        self.writingSpec = encoding
        self.offset = offset
    
    def map_r_to_l(self, c):
        """
        Represents current flowing from right to left in the rotor
        """
        c = c.upper()
        self.offset = (self.offset + 1) % 26 #Spin rotor once
        i = (index(c) + self.offset)  
        encoded = self.writingSpec[i] #encoded version of c according to the wiring specification of the rotor
        encoded_index = index(encoded) #index in alphabet of encoding of c
        return encoded_index

    def map_l_to_r(self, c):
        """
        Represents current flowing from left to right in the rotor, returns encoding of c 
        """
        c = c.upper()
        c_index = index(c)
        c_index += self.offset #add offset to the input contact
        c_offset_char = chr(c_index+65)
        encoded_index = self.inverse_index(c_offset_char) #index in alphabet of encoding of c
        return encoded_index
        
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

    def get_writingSpec(self):
        return self.writingSpec


    def inverse_index(self, c):
        """
        Return the index of c in the writingSpec of the rotor
        """
        return self.writingSpec.index(c)
