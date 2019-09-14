"""
File related to creation, crossover and mutation of the population
"""
import random

#creates an aleatory popuplation, which the 1st and the last cities are equals.
def createPop(origVector):  #origvector -> Thus, the original vector won't be lost
    vector = origVector.copy()     # why not vector=origVector doesn't work?  when .remove(), retira nos 2 objs.
    createdPop = [None] * (len(vector)+1) 

    for i in range(len(vector)):
        x = random.choice(vector)
        if i == 0:
            createdPop[0] = x  # the 1st and the last one city will be equals.
            createdPop[len(vector)] = x
        else:
            createdPop[i] = x        
        vector.remove(x) #remove the city, thus, won't exist the repeated cities.
    return createdPop

def crossover():
    return

def mutation():
    return