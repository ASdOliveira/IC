#------------------------------------------------------------------------------+
#   Arysson Silva de Oliveira
#   Particle Swarm Optimization
#   PPGES-UPE
#
# In this activity, you must optimize Sphere and Rastrigin functions
#------------------------------------------------------------------------------+

from PSO import PSO
import function_opt



initial=[5,5]               # initial starting location [x1,x2...]
bounds=[(-10,10),(-10,10)]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
PSO(function_opt.func1, initial, bounds, num_particles=15, maxiter=30, verbose=True)
