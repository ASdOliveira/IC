"""
University of Pernambuco - PPGES
Travel Salesman Problem using python
Solved by: Arysson Oliveira
Teacher: Carmelo bastos
"""
import fileText
import population
import calculate

listOfCities = fileText.readDB()

cityQtd = 5  #quantity of cities that will be used
popQtd = 4
cities = [None] * cityQtd #create an empty list with cityQtd elements.
pop = []
pop = list(pop)
if (cityQtd != 52):
    for i in range(cityQtd):
        cities[i] = listOfCities[i]
        #print(cities[i][0])
else:
    cities = listOfCities

for i in range(popQtd):
    pop.append(population.createPop(cities))
########################################
fitvalue = 0
bestRoute = []
k = 0
dist = [0,0,0,0,0,0]
stopCondition = False
########### main::
while stopCondition == False :

    for i in range(len(pop)): #calculate the fit value to all vector
        dist = list(dist)
        dist[i] = calculate.fitness(pop[i])
    
    #sort the distance and pop in ascending order from the fit value
    dist, pop = zip(*sorted(zip(dist, pop))) 

    if(fitvalue == 0): #initial value
        fitvalue = dist[0]
        bestRoute = pop[0]
    else:
        if fitvalue < dist[0]:
            fitvalue = dist[0]
            bestRoute = pop[0]
            k = 0
        else:
            cutPointmin = 2
            cutPointmax = 4
            pop = list(pop)
            pop[2],pop[3] = population.crossover(pop[0],pop[1],cutPointmin,cutPointmax)
            print(k)
            k = k + 1
    if k >= 20:
        stopCondition = True
print(fitvalue)
print(bestRoute)