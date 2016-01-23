import os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

ph = os.path.expanduser('~/public_html')

# first set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
# we install the axes x from 0 to 2 and y from -2 to 2
ax = plt.axes(xlim=(0,2), ylim=(-2, 2))
# set background colour
ax.set_axis_bgcolor('black')
# drawing a line
line, = ax.plot([], [], lw=8,color='black')
line1, = ax.plot([], [], lw=16,color='gold')
# drawing two circles with black perimeter and width of five mm
circle, =ax.plot([],[], 'o', markerfacecolor='w', markeredgecolor='black',
markersize=50, markeredgewidth = 1)
circle1, =ax.plot([],[], 'o', markerfacecolor='w', markeredgecolor='red',
markersize=50, markeredgewidth = 1)
# initialization of the line and the two circles: plot the background of each frame
def init():
    line.set_data([], [])
    line1.set_data([], [])
    circle.set_data([],[])
    circle1.set_data([],[])
    return line,line1,circle,circle1

# animation function of cos,tan and the circles. This is called sequentially
def animate(i):
    x = np.linspace(0, 2, 1000)
    x1 = np.linspace(2, 0, 1000)
    y = np.cos(3 * np.pi * (x - 0.01 * i))
    y1 = np.cos(1 *np.pi * (x1 - 0.01 * i))
    #Defining the tan function
    y1 = np.tan(3*np.pi*(x-0.01*i))
    line.set_data(x, y)
    line1.set_data(x1,y1)
    # ploting the two circles on sin and tan functions
    circle.set_data(x,y)
    circle1.set_data(x,y1)
    return line,line1,circle,circle1

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=300, interval=40, blit=True)
# saving the video, and in every second draws 30 frames
anim.save(ph+"/animation_Team5.mp4", fps=30, extra_args=['-vcodec', 'libx264'])