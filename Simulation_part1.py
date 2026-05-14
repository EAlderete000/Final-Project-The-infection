import numpy as np
import matplotlib.pyplot as plt
from definitions import terrain_flat, run_simulation 


"""This file will specifically run summary and states of the functions and simulation.
"""


results = run_simulation(func=terrain_flat, #terrain function
                         traveler_starts= 1, #as many points can be added
                         werewolf_starts= 1,#as many points can be added
                         n_steps=100, #the amount of steps the simulation will run
                         step_size=0.1, #a distance the entity can walk
                         infection_radius=1.0,
                         x_range=(-6, 6),
                         y_range=(-6, 6)
                         ) #distane of the werewolf infection

print(results["summary"])

for i, traveler in enumerate(results["travelers"]):
    start = traveler["path"][0]
    end = traveler["path"][-1]
    print(f"Traveler {i+1}: Start: {start}, End: {end}")

for i, werewolf in enumerate(results["werewolves"]):
    start = werewolf["path"][0]
    end = werewolf["path"][-1]
    print(f"Werewolf {i+1}: Start: {start}, End: {end}")

for i, infected in enumerate(results["infected"]):
    start = infected["path"][0]
    end = infected["path"][-1]
    print(f"Infected {i+1}: Start: {start}, End: {end}")    