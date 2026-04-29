import numpy as np
import matplotlib.pyplot as plt
from definitions import traveler, werewolf, terrain_flat
from image_legend import HandlerLineImage as hli

'''Overview - a simple plat field(function) with 1 traveler and 1 werewolf, which would then have the 
possibility of infecting the traveler which results in 0 travelers 1 werewolf and 1 infected.
The plot would show the path the traveler and werewolf(and infected) take. 

Output summary would showcase the number of travelers, werewolves, and infected at the end of a simulation,
that would go through several iterations(n, which could mean days). Additionally show the probability of
being bit by a werewolf and becoming infected over an iteration of days.'''

#====adjustable variables====#


#====Print-out Summary=====#

#========Scatter-plot========================#


plt.figure(figsize=(10,10))
line,  = plt.plot([1,2],[1.5,3], color="#1f66e0", lw=1.5)
line2,  = plt.plot([1,2],[1,2], color="#efe400", lw=1.5)
line3,  = plt.plot([1,3],[5,2], color="#ff17ff", lw=1.5)
plt.ylabel("y")
plt.xlabel("x")
plt.title("trails of infection")

plt.legend([line, line2, line3], ["", "", ""],
   handler_map={ line: hli("figures/Traveler.png"), line2: hli("figures/Werewolves.png"), line3: hli("figures/Infected.png")}, 
   handlelength=1, labelspacing=0.0, fontsize=100, borderpad=0.15, loc=2, 
    handletextpad=0.1, borderaxespad=0.15)

plt.show()