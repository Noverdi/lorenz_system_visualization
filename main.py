from lorenz_system import export_states
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 100
w.resize(1920, 1080)
w.setWindowTitle('pyqtgraph openGL : Lorenz System Visualization Test')
w.show()

# color
n = len(export_states())
r = np.linspace(0.5, 0.4, n)
g = np.linspace(0.4, 1, n)
b = np.linspace(1, 0, n)
h = np.linspace(0.15, 0.4, n)  #np.array( [0.5] * n )
color = np.vstack((r,g,b,h)).transpose()

# set point and color to range of point into the graph
pts = export_states()
plt = gl.GLLinePlotItem(pos=pts[:0], antialias=True)
plt.color = color[:0]  #(0.5, 0.5, 0.5, 0.5)
plt.translate(0,0,-30)
w.addItem(plt)

index = 0
def update():
    global plt, pts, index
    index += 5
    plt.setData(pos=pts[:index], antialias=True)
    plt.color = color[:index]


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)


## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()