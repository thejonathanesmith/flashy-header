import numpy as np
import matplotlib.animation as animation
from matplotlib import pyplot
import seaborn as snes
import colorcet as cc

bck = "black"
pyplot.rcParams['axes.facecolor'] = bck
pyplot.rcParams['savefig.facecolor'] = bck
fig, g = pyplot.subplots(figsize=(16,4)) # sets the overall size (x,y)
pyplot.subplots_adjust(left = 0.0, right = 1.0, top = 1.0, bottom = 0.0)

# Colorcet colormaps
l4c = cc.cm.kgy
ctd = 0 # Counter

def update(*args) :
  global ctd,cmp
  def cmp_choice(): # Randomly picking a colormap
      cmp = np.random.choice([l4c]) #limited choices to something more in my site's color schem
      return cmp
  pyplot.clf()
  if ctd%2 == 0 : # 4 frames with the same colormap
     cmp = cmp_choice()

  mt = np.random.uniform(low = 0, high = 128, size=(4,16)) #plotting matrix

  snes.heatmap(mt, annot = False, cmap=cmp, linecolor = "black", linewidths=0.010,
              square = False,   cbar = False)
  ctd +=1
  return ()

def init() :
    return()

#limited the number of frames to 8 and the fps to 4
#so that the image would not be too fast and distracting for a header
anim = animation.FuncAnimation(fig, update, init_func=init, blit = True, frames=8, repeat = False)

sf = "colors"+".gif"
Sname = "C:\\Users\Me\Desktop\_" + sf
anim.save(Sname, writer="imagemagick")

# You must have imagemagick installed in you computer :
# https://www.imagemagick.org/script/index.php
