import numpy as np
import matplotlib.pyplot as plt

import matplotlib.lines
from matplotlib.transforms import Bbox, TransformedBbox
from matplotlib.legend_handler import HandlerBase
from matplotlib.image import BboxImage


#=======Entity/walker functions ====#
def random_walk(func : callable,
                start: tuple,
                n_steps: int,
                step_size: float) -> np.array:
    """This function applies a random walk in which would move points +1 or - 1.

    Args:
        func (callable): terrain function
        start (tuple): starting position (x,y) of the walker
        n_steps (int): _description_
        step_size (float): _description_

    Returns:
        np.array: _description_
    """
    
    x,y = start
    path = [(x,y)]

    for _ in range(n_steps):
        current = func(x,y)

        new_x = x + np.random.uniform(-step_size, step_size)
        new_y = y + np.random.uniform(-step_size, step_size)
        new_value = func(new_x, new_y)

        if new_value < current:
            x,y = new_x, new_y
            path.append((x,y))

    return np.array(path)


def traveler(func : callable,
           start : tuple , 
           n_steps : int,
           step_size : int) -> np.array:
    """This a function for a random walker along any contour function given. it will follow a path
    That is near the pits or minimum of a function. It will take a number of travelers(like 1 or 20 or more)


    Args:
        func (callable): The function of the walker to use, for example... paraboloid.
        start (tuple): Starting point of the walker
        n_steps (int): The number of steps the walker will take, can be customizable
        step_size (int): the step size the walker will take, can be customizable

    Returns:
        Random_walk function with traveler parameters 
    """

    return random_walk(func, start, n_steps, step_size)

def werewolf(func : callable,
           start : tuple , 
           n_steps : int,
           step_size : int) -> np.array:
    """This a function for a random werewolf

    Args:
        func (callable): The function of the walker to use, for example... paraboloid.
        start (tuple): Starting point of the walker
        n_steps (int): The number of steps the walker will take, can be customizable
        step_size (int): the step size the walker will take, can be customizable

    Returns:
        Random_walk function with werewolf parameters 
    """

    return random_walk(func, start, n_steps, step_size)

#if traveler is within range of werewolf, traveler = infected function.
def infected(func : callable,
           start : tuple , 
           n_steps : int,
           step_size : int) -> np.array:
    """This a function for a random traveler that has been infected by a werewolf due to being within range of the werewolf.
    Since the traveler is infected - it will act the same way as a werewolf would, which even includes infecting other travelers

    Args:
        func (callable): The function of the walker to use, for example... paraboloid.
        start (tuple): Starting point of the walker
        n_steps (int): The number of steps the walker will take, can be customizable
        step_size (int): the step size the walker will take, can be customizable

    Returns:
        Random_walk function with infected parameters 
    """
    return random_walk(func, start, n_steps, step_size)

#=======Additional attributes====#
#================================#
#the infections i want to implement on the traveler

def distance(point1, 
             point2):
    """This is a function to calculate the distance between two points, which will be used to determine if a traveler is within range of a werewolf and thus becomes infected.

    Args:
        point1 (tuple): The first point (x,y)"""
    
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def is_infected(traveler_pos, 
                werewolf_pos, 
                infection_radius):
    """This is a function to determine if a traveler is infected by a werewolf based on their positions and the infection radius."""

    return distance(traveler_pos, werewolf_pos) <= infection_radius


#========Terrain functions======#
#These are just a variety of functions 

#will be used for part 1 only
def terrain_flat(x,y):
    return np.cos(x**2 + y**2)

#below will be used for part 2 - 3(?)

def terrain_complex():
    pass

#Himmelblau function
def terrain_complex(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

#==========The simulation Function=======#

def run_simulation(func: callable,
                   traveler_starts: list,
                   werewolf_starts: list,
                   n_steps: int,
                   step_size: float,
                   infection_radius: float):

    '''This is basically the entire 'brains' to how the simulation will run. 

The werewolf infection simulation...

Travlers will become infected if they come within infection_radius of any werewolf or infected traveler. spreading like a virus'''

    travelers = []
    werewolves = []

    #paths
    for start in traveler_starts:
        travelers.append({"status": "traveler", "path": random_walk(func, start, n_steps, step_size)})

    for start in werewolf_starts:
        werewolves.append({"status": "werewolf", "path": random_walk(func, start, n_steps, step_size)})

    #Need to run through to check if infections need to take place.
    for step in range(n_steps):
        for traveler in travelers:
            if traveler["status"] == "infected":
                continue
            traveler_pos = traveler["path"][step]

            for werewolf in werewolves:
                werewolf_pos = werewolf["path"][step]
                if is_infected(traveler_pos, 
                               werewolf_pos, 
                               infection_radius):
                    traveler["status"] = "infected"
                    break

    #final list
    final_travelers = []
    final_infected = []

    for traveler in travelers:
        if traveler["status"] == "traveler":
            final_travelers.append(traveler)
        else:
            final_infected.append(traveler)

    summary = {
        "initial_travelers": len(travelers),
        "initial_werewolves": len(werewolves),
        "final_travelers": len(final_travelers),
        "final_infected": len(final_infected),
        "Therefore...final_werewolves": len(werewolves) + len(final_infected)} #since infected also act as werewolves

    return{
    "travelers": final_travelers,
    "infected": final_infected,
    "werewolves": werewolves,
    "summary": summary,
    }

# Source - https://stackoverflow.com/a/42169584
# Posted by ImportanceOfBeingErnest, modified by community. See post 'Timeline' for change history
# Retrieved 2026-04-27, License - CC BY-SA 4.0
class HandlerLineImage(HandlerBase):

    def __init__(self, path, space=15, offset = 10 ):
        self.space=space
        self.offset=offset
        self.image_data = plt.imread(path)        
        super(HandlerLineImage, self).__init__()

    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):

        l = matplotlib.lines.Line2D([xdescent+self.offset,xdescent+(width-self.space)/3.+self.offset],
                                     [ydescent+height/2., ydescent+height/2.])
        l.update_from(orig_handle)
        l.set_clip_on(False)
        l.set_transform(trans)

        bb = Bbox.from_bounds(xdescent +(width+self.space)/3.+self.offset,
                              ydescent,
                              height*self.image_data.shape[1]/self.image_data.shape[0],
                              height)

        tbb = TransformedBbox(bb, trans)
        image = BboxImage(tbb)
        image.set_data(self.image_data)

        self.update_prop(image, orig_handle, legend)
        return [l,image]