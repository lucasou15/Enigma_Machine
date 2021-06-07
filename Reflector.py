from helpers import *

class Reflector:
    def __init__(self, s):
        """
        Creates an instance of Reflector with writing specification 
        """
        self.writingSpec = s 

    def map(self, c):
        """
        Encodes c according to the writing specification of the reflector
        """
        return self.writingSpec[index(c.upper())]
