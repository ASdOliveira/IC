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
popQtd = 5
cities = [] #create an empty list with cityQtd elements.
pop = []
pop = list(pop)
if (cityQtd != 52):
    for i in range(cityQtd):
        #cities[i] = listOfCities[i]
        cities.append(listOfCities[i])
        #print(cities[i][0])
else:
    cities = listOfCities

for i in range(popQtd):
    pop.append(population.createPop(cities))
########################################
fitvalue = 0
bestRoute = []
k = 0
j = 0
dist = [0]*popQtd
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
        if dist[0] < fitvalue:  
            fitvalue = dist[0]
            bestRoute = pop[0]
            k = 0
            j = j + 1
            print ("j value: " + str(j))
        else:
            ##cutPointmin = 2
            cutPointmax = 4
            pop = list(pop)
            pop[2] = population.crossover(pop[0],pop[1])
            pop[3] = population.crossover(pop[1],pop[0])
            print("k value: " + str(k))
            print ("fitvalue: " + str(fitvalue))
            k = k + 1
            j = 0
    if k >= 30: #debugaaaar
        stopCondition = True
print("Last Fitvalue: " + str(fitvalue))
print("Last BestRoute" + str(bestRoute))