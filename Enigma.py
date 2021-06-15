from Rotor import *
from Reflector import *
from helpers import *
from collections import deque
#############################################
#    Defines main Enigma machine class that #
#    represents the main functionality of   #
#    the enciphering process                #
#############################################

#TODO: Need to define global DS to store the different rotors and reflectors by name for input purposes
#TODO: Need to change the constructor for the plugboard once we take in user input for its construction

#Defines the rotors that we are able to choose from
ROTORS = [("Rotor I", Rotor("Rotor I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", 0)), ("Rotor II", Rotor("Rotor II", "AJDKSIRUXBLHWTMCQGZNPYFVOE", 0)), ("Rotor III",Rotor("Rotor III", "BDFHJLCPRTXVZNYEIWGAKMUSQO", 0)), ("Rotor IV", Rotor("Rotor IV", "ESOVPZJAYQUIRHXLNFTGKDCMWB", 0)), ("Rotor V", Rotor("Rotor V", "VZBRGITYUPSDNHLXAWMJQOFECK", 0)), ("Rotor VI", Rotor("Rotor VI", "JPGVOUMFYQBENHZRDKASXLICTW", 0)), ("Rotor VII", Rotor("NZJHGRCXMYSWBOUFAIVLPEKQDT", 0)), ("Rotor VIII", Rotor("FKQHTLXOCBJSPDZRAMEWNIUYGV", 0))]

#Defines the reflector we are able to choose from
REFLECTORS = [("Reflector B", Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")), ("Reflector C", Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL"))]



class Enigma:
    def __init__(self, rotor1, rotor2, rotor3, refls): #TODO: Add plugboard parameter and attribute when that's dones
        self.rotors = [rotor1, rotor2, rotor3] #array of Rotor objects that specify the rotors to be used from left to right
        self.reflector = refl #relector that will be used

    def encipher_char(self, c):
        """
        Returns the encoding of char c given the settings of the enigma machine
        """
        #TODO: First have to pass c through the plugoard, do this once we have that implemented

        #Pass c through the rotors
        #TODO: Stepping of rotor
        c = c.upper()
        #step the rightmost rotor
        rot = self.rotors[2]
        self.rotors[2].set_offset(r.get_offset()+1)
        #check if we should step second rotor
        enc = self.rotors[2].map_r_to_l(c)
        enc = self.rotors[1].map_r_to_l(enc)
        enc = self.rotors[0].map_r_to_l(enc)
        enc = self.reflector.map(enc)
        enc = self.rotors[0].map_l_to_r(enc)
        enc = self.rotors[1].map_l_to_r(enc)
        enc = self.rotors[2].map_l_to_r(enc)
        return enc

    def encipher_text(self, str):
        """
        Returns the encoding of string str given the settings of the enigma machine
        """
        pass




print("Welcome to Enigma!")
print("Please select the rotors you would like to use, you can choose from the following:")
for i in range(len(ROTORS)):
    print(ROTORS[i][0] + " with writing specification " + ROTORS[i][1].get_writingSpec())

rotor_selec = deque()
rotor_selec_names = []
i = 0
while i <= 2:
    rot = input("Rotor in position " + str(i+1) + ": ")
    if rot in rotor_selec_names:
        print("That rotor has already been selected!")
    elif rot == "Rotor I":
        rotor_selec.appendleft(ROTORS[0][1])
        rotor_selec_names.append(rot)
        i+= 1
    elif rot == "Rotor II":
        rotor_selec.appendleft(ROTORS[1][1])
        rotor_selec_names.append(rot)
        i+= 1
    elif rot == "Rotor III":
        rotor_selec.appendleft(ROTORS[2][1])
        rotor_selec_names.append(rot)
        i+= 1
    elif rot == "Rotor IV":
        rotor_selec.appendleft(ROTORS[3][1])
        rotor_selec_names.append(rot)
        i+= 1
    elif rot == "Rotor VI":
        rotor_selec.appendleft(ROTORS[4][1])
        rotor_selec_names.append(rot)
        i+= 1
    elif rot == "Rotor VI":
        rotor_selec.appendleft(ROTORS[5][1])
        rotor_selec_names.append(rot)
        i+= 1
    elif rot == "Rotor VII":
        rotor_selec.appendleft(ROTORS[6][1])
        rotor_selec_names.append(rot)
        i+= 1
    elif rot == "Rotor VIII":
        rotor_selec.appendleft(ROTORS[7][1])
        rotor_selec_names.append(rot)
        i+= 1
    else:
        print("Please choose a valid rotor")
        

    
print("Please select the reflector you would like to use, you can choose from the following:")
for i in range(len(REFLECTORS)):
    print(REFLECTORS[i][0] + " with writing specification " + REFLECTORS[i][1].get_writingSpec())

while True:
    r = input("Reflector: ")
    if r == "Reflector B":
        refl = REFLECTORS[0][1]
        break
    elif r == "Reflector C":
        refl = REFLECTORS[1][1]
        break
    else:
        print("Please enter a valid reflector!")

#TODO: Plugboard input
machine = Enigma(rotor_selec[2], rotor_selec[1], rotor_selec[0], refl)
