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

def crossover(v1,v2,cutPointmin,cutPointmax):
    vec1 = v1[:cutPointmin] + v2[cutPointmin:cutPointmax] + v1[cutPointmax:]
    vec2 = v2[:cutPointmin] + v1[cutPointmin:cutPointmax] + v2[cutPointmax:]   
    return vec1, vec2


def mutation(vector):
    return


#Auxiliar function, to detect repeated items

"""
vetor1 = [1,2,3,4,5,1]
vetor2 = [2,1,4,5,3,2]
cutPointmin = 2
cutPointmax = 4
test1,test2 = crossover(vetor1,vetor2,cutPointmin,cutPointmax)"""