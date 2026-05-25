import numpy as np
import matplotlib.pyplot as plt
from definitions import terrain_1, terrain_1, run_simulation 


"""This file will specifically run summary and states of the functions and simulation.
"""


results = run_simulation(func=terrain_1, #terrain function
                         traveler_starts= 10, #as many points can be added
                         werewolf_starts= 5,#as many points can be added
                         n_steps=100, #the amount of steps the simulation will run
                         step_size=0.5, #a distance the entity can walk
                         infection_radius=1.0, #distane of the werewolf infection
                         x_range=(-6, 6), #The size of the terrain x-dir
                         y_range=(-6, 6) #The size of the terrain y-dir
                         )

#Summary of the simulation results

#intial and final states of the travelers, werewolves, and infected.
print(results["summary"])

#The paths in which the travelers, werewolves, and infected took, starting and end points.
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

#Probability of getting an infection
total_travelers = len(results["travelers"])
total_werewolves = len(results["werewolves"])
total_infected = len(results["infected"])
infection_probability = total_infected / (total_travelers + total_werewolves) * 100 if (total_travelers + total_werewolves) > 0 else 0 #Finding the probability but if infected is 0, then probability in becoming a werewolf is 0%.%.
print(f"Probability of getting infected: {infection_probability:.2f}%")  