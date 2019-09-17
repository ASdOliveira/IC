"""
File related to creation, crossover and mutation of the population
"""
import random
import fileText

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

def crossover(parent1,parent2):
    #vec1 = v1[:cutPointmin] + v2[cutPointmin:cutPointmax] + v1[cutPointmax:]
    #vec2 = v2[:cutPointmin] + v1[cutPointmin:cutPointmax] + v2[cutPointmax:]  
    child = []
    childP1 = []
    childP2 = []
   
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])
        
    for i in range(len(parent2)):
        if parent2[i] not in childP1:
            if parent2[i] not in childP2:
                childP2.append(parent2[i]) 

    child = childP1 + childP2
    child.append(child[0])
   # fileText.writeDB("child" + str(child)) 
    return child


def mutation(vector):
    i1 = random.randint(1,(len(vector) - 2)) #don't mutate the head and tail values
    i2 = random.randint(1,(len(vector) - 2)) 
    temp = vector[i1]
    vector[i1] = vector[i2]
    vector[i2] = temp
    return vector

