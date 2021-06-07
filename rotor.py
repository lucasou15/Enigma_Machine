
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
    def map_r_to_l(self, c):
        """
        Represents current flowing from right to left in the rotor
        """
        c = c.upper()
        self.offset += 1 #Spin rotor once
        i = (self.index(c) + self.offset)  % 26
        encoded = self.writingSpec[i] #encoded version of c according to the wiring specification of the rotor
        encoded_index = self.index(encoded) #index in alphabet of encoding of c
        return encoded_index

    
    #TODO: Insert params
    def map_l_to_r(self, c):
        """
        Represents current flowing from left to right in the rotor, returns encoding of c 
        """
        c = c.upper()
        c_index = self.index(c)
        c_index += self.offset #add offset to the input contact
        c_offset_char = chr(c_index+65)
        encoded_index = self.inverse_index(c_offset_char) #index in alphabet of encoding of c
        return encoded_index
        

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

    def get_writingSpec(self):
        return self.writingSpec

    def index(self, c):
        """
        Return the index in the alphabet of character c
        """
        return ord(c) - 65

    def inverse_index(self, c):
        """
        Return the index of c in the writingSpec of the rotor
        """
        return self.writingSpec.index(c)