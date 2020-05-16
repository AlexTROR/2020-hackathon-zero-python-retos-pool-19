#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen):
    res = ""
    char = 0
    #passLen = 10

    for i in range(passLen):
        char = random.randint(0,1)
        if char == 1:
            aux = random.randint(33, 126)
            aux = chr(aux)
        else:
            aux = random.randint(0, 9)
        
        res = res + str(aux)
    
    return res
            

#length = input('Introduce longitud de la password: ')
#length = int(length)
#password = RandomPasswordGenerator(length)
#print(password)
