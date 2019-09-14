"""
University of Pernambuco - PPGES
Travel Salesman Problem using python
Solved by: Arysson Oliveira
Teacher: Carmelo bastos
"""
import fileText
import calculate

listOfCities = fileText.readDB()

cityQtd = 5  #quantity of cities that will be used
cities = [None] * cityQtd #create an empty list with cityQtd elements.

if (cityQtd != 52):
    for i in range(cityQtd):
        cities[i] = listOfCities[i]
        #print(cities[i][0])
else:
    cities = listOfCities

