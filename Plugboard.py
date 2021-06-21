from helpers import *
##############################################
#    Defines Plugboard class that represents #
#    the assignment of letter arr to be    #
#    switched in the enciphering process     #
##############################################
class PlugBoard:
    def __init__(self, arr): #aatribute le tengo que decir las parejas de letras
        # arr = arr.upper() #CORREGIR
        # self.pairs =  {
        #     "A": "H", 
        #     "N": "S", 
        #     "X": "U", 
        #     "C": "Z", 
        #     "J": "D", 
        #     "Q": "V", 
        #     "K": "O", 
        #     "B": "L", 
        #     "E": "W", 
        #     "G": "T", 
        #     "M": "Y", 
        #     "F": "P", 
        #     "R": "I"
        # }
        # letter = input()
        # for arr in arr.values(): 
        #     if input() == letter:
        #         return (arr)
        #     else:
        #         return (arr.keys())
        
        # num = index(input())
        # for arr in list(arr):
        #     if (num % 2) == 0:
        #         return list(arr(num + 1))
        #     else:
        #         return list(arr(num - 1))


    #encypher le tengo que decir que las cambie o sea un function que cambie a a p





#Getter que me diga cual es la pareja de cada letra si le pregunto


#setter para que pueda cambiar la pareja de algunas letras

        self.pairs = {}
        for lst in arr:
            self.pairs[lst[0]] = lst[1]
            self.pairs[lst[1]] = lst[0]

    
    def encipher(self, c):
        if c in self.pairs:
            return self.pairs[c]
        return c
        
    

            
