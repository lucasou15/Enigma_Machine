
#############################################
#    Defines Rotor class that represents    #
#    the different rotors that can be used  #
#    in the enigma machine                  #
#############################################

class Rotor:
    #TODO: Insert params and attributes
    def __init__(self, s):
        """
        Creates an instance of Rotor
        """
        self.writingSpec = s
    
    #TODO: Insert params
    def map_r_to_l(self):
        """
        Represents current flowing from right to left in the rotor
        """
    
    #TODO: Insert params
    def map_l_to_r(self):
        """
        Represents current flowing from left to right in the rotor
        """
    #TODO: Insert params
    def advance_rotor(self):
        """
        Simulates the stepping of the rotor after a mapping 
        """

    #TODO: Insert params
    def set_top_letter(self):
        """
        Allows user to set the top letter (starting position/offset) of the rotor
        """
