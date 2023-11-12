import sympy as sp
import numpy as np
import copy
import matplotlib.pyplot as plt
def setLinesv3(size):
    delta = 0.025
    x = np.arange(-size, size, delta)
    y = np.arange(-size, size, delta)
    X, Y = np.meshgrid(x, y)
    Z = np.arctan(2*Y/(1-X*X-Y*Y))
    fig, ax = plt.subplots()
    CS = ax.contour(X, Y, Z, 20, cmap ='plasma')
    ax.set_title('Level set')
setLinesv3(5)
plt.savefig("CalcT1.png")