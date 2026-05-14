import numpy as np
import matplotlib.pyplot as plt
from definitions import terrain_flat,run_simulation 


"""This file will specifically run summary and states of the functions and simulation - plots will show up in part two which would
Otherwise be data but visualized."""

results = run_simulation(func=terrain_flat, #terrain function
                         traveler_starts=[(0,0),(0,0)], #as many points can be added
                         werewolf_starts=[(0,0)],#as many points can be added
                         n_steps=100, #the amount of steps the simulation will run
                         step_size=0.1, #a distance the entity can walk
                         infection_radius=1.0) #distane of the werewolf infection

print(results["summary"])