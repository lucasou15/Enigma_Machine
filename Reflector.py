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
        encoded = self.writingSpec[index(c.upper())]
        print("Encoding in reflector " + c + " becomes " + encoded)
        return encoded

    def get_writingSpec(self):
        return self.writingSpec
