import unittest
from Rotor import *

VERBOSE = True

class TestRotor(unittest.TestCase):
    def test_encoding_single(self):
        """
        Tests the mappings of "A" when passed into rotor I of enigma
        """
        print("Running test_encoding_single...")
        rotor_I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 0) #create Rotor object with encoding consistent with rotor I of enigma
        mappings = "KMFLGDQVZNTOWYHXUSPAIBRCJE"
        for i in range(26):
            if VERBOSE:
                print("Checking A -> " + str(mappings[i]))

            enc = rotor_I.map_r_to_l("A")
            self.assertEqual(enc, ord(mappings[i])-65)