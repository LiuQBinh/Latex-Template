from matplotlib import pylab
from pylab import *
import sys
epsilon = sys.float_info.epsilon

xvalues, yvalues = meshgrid(arange(0, 3, 0.1), arange(0, 3, 0.1))
xdot = 2 * xvalues + 4 * yvalues
ydot = - 2 * xvalues - 2 * yvalues

streamplot(xvalues, yvalues, xdot, ydot)
show()