"""
File destined to calc functions.
"""
import math

def euclidianDistance(v1, v2):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(v1, v2)]))
    return distance

#Calculate the fitness result for te distance
def fitness(vector): 
	distancia = 0
	for i in range(len(vector)-1):
		distancia += euclidianDistance(vector[i][1:],vector[i+1][1:])
	return distancia