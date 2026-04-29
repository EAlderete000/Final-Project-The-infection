# Source - https://stackoverflow.com/a/42169584
# Posted by ImportanceOfBeingErnest, modified by community. See post 'Timeline' for change history
# Retrieved 2026-04-27, License - CC BY-SA 4.0

'''An attempt to add some images to the legend to showcase....the werewolves'''

import matplotlib.pyplot as plt
import matplotlib.lines
from matplotlib.transforms import Bbox, TransformedBbox
from matplotlib.legend_handler import HandlerBase
from matplotlib.image import BboxImage

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


plt.figure(figsize=(10,10))
line,  = plt.plot([1,2],[1.5,3], color="#1f66e0", lw=1.5)
line2,  = plt.plot([1,2],[1,2], color="#efe400", lw=1.5)
line3,  = plt.plot([1,3],[5,2], color="#ff17ff", lw=1.5)
plt.ylabel("Werewolves")

plt.legend([line, line2, line3], ["", "", ""],
   handler_map={ line: HandlerLineImage("figures/Traveler.png"), line2: HandlerLineImage("figures/Werewolves.png"), line3: HandlerLineImage("figures/Infected.png")}, 
   handlelength=1, labelspacing=0.0, fontsize=100, borderpad=0.15, loc=2, 
    handletextpad=0.1, borderaxespad=0.15)

plt.show()
