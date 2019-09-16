"""
University of Pernambuco - PPGES
Travel Salesman Problem using python
Solved by: Arysson Oliveira
Teacher: Carmelo bastos
"""
import fileText
import population
import calculate

#Import the cities
listOfCities = fileText.readDB()

fileText.writeDB("initializing")

############### "Defines" #####################
cityQtd = 5  #quantity of cities that will be used
popQtd = 5
NumInteracoes  = 30
fitvalue = 0
bestRoute = []
k = 0
j = 0
dist = [0]*popQtd
stopCondition = False

cities = [] #create an empty list with cityQtd elements.
pop = []
pop = list(pop)


#carry the amount of city chosen 
if (cityQtd != 52):
    for i in range(cityQtd):
        cities.append(listOfCities[i])
else:
    cities = listOfCities

for i in range(popQtd):
    pop.append(population.createPop(cities))
########################################

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
            fileText.writeDB("j value: " + str(j)) #prints into TXT
        else:
            ##cutPointmin = 2
            cutPointmax = 4
            pop = list(pop)
            pop[2] = population.crossover(pop[0],pop[1])
            pop[3] = population.crossover(pop[1],pop[0])
            fileText.writeDB("k value: " + str(k))
            fileText.writeDB ("fitvalue: " + str(fitvalue))
            k = k + 1
            j = 0
    if k >= NumInteracoes: 
        stopCondition = True
fileText.writeDB("Last Fitvalue: " + str(fitvalue))
fileText.writeDB("Last BestRoute" + str(bestRoute))