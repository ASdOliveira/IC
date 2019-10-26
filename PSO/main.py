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

#parameters that were given
particles = 30
dimensions = 2
max_iter = 300
simut_quantity = 1             #The quantity of the process will run
rastriginBound = [-5.12, 5.12] #according the article sent
sphereBound = [-100, 100]      #according the article sent

#auxiliar variables
initial_position_sphere = [] #contains the particle's initial position
initial_position_rastrigin = []
sphere_bounds = []
rastrigin_bounds = []

#fileText.writeDB("Initializing...")

#tools that will help to fill the initial and bounds variables
def initialize_particles():
    for i in range(0,dimensions): 
        initial_position_sphere.append(random.random()*sphereBound[1])
        initial_position_rastrigin.append(random.random()*rastriginBound[1])
        sphere_bounds.append(sphereBound)
        rastrigin_bounds.append(rastriginBound)

for i in range(0,simut_quantity):

    print('Initializing Particles')
    initialize_particles()
    print('Initializing sphere')
    #PSO(function_opt.sphere, initial_position_sphere, sphere_bounds, particles, max_iter, verbose=True)
    print('Initializing Rastrigin')
    PSO(function_opt.rastrigin,initial_position_rastrigin, rastrigin_bounds, particles, max_iter, verbose=True,filename='Rastrigin')