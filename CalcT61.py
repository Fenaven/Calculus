import matplotlib.pyplot as plt
import numpy as np
def setLinesXY(size=5, lines=20, delta=0.025, fill = False):
    x = np.arange(-size, size, delta)
    y = np.arange(-size, size, delta)
    X, Y = np.meshgrid(x, y)
    Z = X*Y*(6-X-Y)
    fig, ax = plt.subplots()
    if fill:
        CS = ax.contourf(X, Y, Z, lines, cmap ='gist_rainbow')
    else:
        CS = ax.contour(X, Y, Z, lines, cmap ='gist_rainbow')
    ax.set_title('Level set, XY')
def setLinesZX(size=5, lines=20, delta=0.025, fill = False):
    x = np.arange(-size, size, delta)
    y = np.arange(-size, size, delta)
    X, Y = np.meshgrid(x, y)
    Z = X*Y*(6-X-Y)
    fig, ax = plt.subplots()
    if fill:
        CS = ax.contourf(Y, Z, X, lines, cmap ='gist_rainbow')
    else:
        CS = ax.contour(Y, Z, X, lines, cmap ='gist_rainbow')
    ax.set_title('Level set, XZ')
def setLinesZY(size=5, lines=20, delta=0.025, fill = False):
    x = np.arange(-size, size, delta)
    y = np.arange(-size, size, delta)
    X, Y = np.meshgrid(x, y)
    Z = X*Y*(6-X-Y)
    fig, ax = plt.subplots()
    if fill:
        CS = ax.contourf(X, Z, Y, lines, cmap ='jet')
    else:
        CS = ax.contour(X, Z, Y, lines, cmap ='jet')
    ax.set_title('Level set, YZ')
size = 10
delta = 0.01
lines = 100
fill = False
setLinesXY(size=size, lines=lines, delta=delta, fill=fill)
plt.savefig("LineSetXY_61.png")
setLinesZX(size=size, lines=lines, delta=delta, fill=fill)
plt.savefig("LineSetXZ_61.png")
setLinesZY(size=size, lines=lines, delta=delta, fill=fill)
plt.savefig("LineSetYZ_61.png")