#------------------------------------------------------------------------------+
#   Arysson Silva de Oliveira
#   Particle Swarm Optimization
#   PPGES-UPE
#
# In this activity, you must optimize Sphere and Rastrigin functions
#------------------------------------------------------------------------------+

from PSO import PSO
import function_opt
import random
import fileText
import plot

#parameters that were given
particles = 30
dimensions = 30
max_iter = 10000
simut_quantity = 1             #The quantity of the process will run
rastriginBound = [-5.12, 5.12] #according the article sent
sphereBound = [-100, 100]      #according the article sent
file1 = 'Sphere'
file2 = 'Rastrigin'

#auxiliar variables
initial_position_sphere = [] #contains the particle's initial position
initial_position_rastrigin = []
sphere_bounds = []
rastrigin_bounds = []

#fileText.writeDB("Initializing...")

#tools that will help to fill the initial and bounds variables
def initialize_particles():
    for i in range(0,dimensions): 
        initial_position_sphere.append(random.random()*sphereBound[random.randint(0,1)])
        initial_position_rastrigin.append(random.random()*random.randint(0,1))
        sphere_bounds.append(sphereBound)
        rastrigin_bounds.append(rastriginBound)

for i in range(0,simut_quantity):

    print('Initializing Particles')
    initialize_particles()
    print('Initializing Sphere PSO')
    PSO(function_opt.sphere, initial_position_sphere, sphere_bounds, particles, max_iter, verbose=True,filename=file1)
    print('Initializing Rastrigin PSO')
    PSO(function_opt.rastrigin,initial_position_rastrigin, rastrigin_bounds, particles, max_iter, verbose=True,filename=file2)
    print('END')

#plot.plot(fileText.readDB(file1,max_iter))
#plot.plot(fileText.readDB(file2,max_iter))