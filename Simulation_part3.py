import numpy as np
import matplotlib.pyplot as plt
from definitions import infected, traveler, werewolf, terrain_flat , HandlerLineImage
from matplotlib import colormaps

import matplotlib.lines
from matplotlib.transforms import Bbox, TransformedBbox
from matplotlib.legend_handler import HandlerBase
from matplotlib.image import BboxImage

'''Overview - Part two of the assignment, Creating visual representation of Simulation part 1. 

Output summary would showcase the number of travelers, werewolves, and
 infected at the end of a simulation. Additionally show the probability of
being bit by a werewolf and becoming infected over an iteration of days.
 Additionally showing visual outputs of histograms of the number of travelers, 
 werewolves, and infected over time. And contour plots to show the paths of the travelers, werewolves, and infected.'''


def main():
    #======Adjustable values======#
    grid_size = 700
    sample_size = 10_000 #steps
    step_size = 1
    x_min, x_max = -6, 6
    y_min, y_max = -6, 6

    #x and y and gridsize
    x = np.linspace(x_min,x_max, grid_size)
    y = np.linspace(y_min,y_max, grid_size)

    #Meshgrid to achieve (x,y) pairs to then, plot
    X, Y = np.meshgrid(x,y)

    #Flat(mostly) Terrain function
    flatZ = terrain_flat(X,Y)

    #Random sampling - creations a random x and y coordinates for travelers and werewolves to start at
    random_x = np.random.uniform(x_min, x_max, int(sample_size))
    random_y = np.random.uniform(y_min, y_max, int(sample_size))

    #=====Traveler, infected and werewolf=======#
    werewolf_path = werewolf(terrain_flat, (random_x[0], random_y[0]), n_steps = sample_size, step_size = step_size)
    werewolf_path = np.array(werewolf_path)#Converts to numpy array
    traveler_path = traveler(terrain_flat, (random_x[1], random_y[1]), n_steps = sample_size, step_size = step_size)
    traveler_path = np.array(traveler_path) #Converts to numpy array
    '''infected_path = infected(terrain_flat, (random_x[2], random_y[2]), n_steps = sample_size, step_size = step_size)
    infected_path = np.array(infected_path) #Converts to numpy array''' #there should not be an infected

    #====Print-out Summary=====#
    

#========Scatter-plot on top of contour========================#

    plt.figure(figsize=(12,10))
    heatmap = plt.contourf(X, Y, flatZ, levels = 100, cmap = "Blues", alpha = 0.5)
    
    traveler_path= plt.plot(traveler_path[:,0], 
                                traveler_path[:,1], 
                                color="#216df1", 
                                lw=1.0)

    werewolf_path= plt.plot(werewolf_path[:,0], 
                                werewolf_path[:,1], 
                                color="#efe400", 
                                lw=1.0)

    '''infected_path= plt.plot(infected_path[:,0], 
                                infected_path[:,1], 
                                color="#ff17ff", 
                                lw=1.0)''' # there should not be an infected path
    
    plt.ylabel("y")
    plt.xlabel("x")
    plt.title("trails of infection")
    plt.colorbar(heatmap)
    #plt.legend()
    plt.show()

'''    This is a visualized legend for the plot

    #its pulling from the image_kegend.py which.. i dont want
    #i want to motify all the plots here... while having the image_legend file be universal
    #for all parts...
    print(traveler_path)
    plt.legend(
        [traveler_path, werewolf_path, infected_path],
        ["", "", ""],
        handler_map={
        traveler_path: HandlerLineImage("figures/Traveler.png"), 
        werewolf_path: HandlerLineImage("figures/Werewolves.png"), 
        infected_path: HandlerLineImage("figures/Infected.png")
        }, 
        handlelength=1, 
        labelspacing=0.0, 
        fontsize=100, 
        borderpad=0.15, 
        loc=2, 
        handletextpad=0.1, 
        borderaxespad=0.15,
        
    )

    plt.show()'''

if __name__ == "__main__":
    main()