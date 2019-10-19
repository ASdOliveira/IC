#File destinated to fuctions that will be optimized

import math

def sphere(x):
    total=0
    for i in range(len(x)):
        total+=x[i]**2
    return total

def rastrigin(x):
    total = 0
    for i in range(len(x)):
        total +=  (x[i]**2) - 10*(math.cos(2*math.pi*x[i])) + 10
    return total