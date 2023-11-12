import sympy as sp
import numpy as np
import copy
import matplotlib.pyplot as plt

sp.var('x, y')
x, y = sp.symbols('x y')

z = x*y*(6-x-y) #function definition

dzdx = sp.diff(z, x)
dzdy = sp.diff(z, y)
dzx = lambda a, b : float(dzdx.evalf(subs={x:a, y:b}))
dzy = lambda a, b : float(dzdy.evalf(subs={x:a, y:b}))
zval = lambda a, b: float(z.evalf(subs={x:a, y:b}))
alpha = lambda a : 1/2 + a/(2+2*np.abs(a))

pointsx = []
pointsy = []
difs = []
dif = 0
counter = 0
thresh = 0.0000001
start = [3, 0.1]
decay = 0.01
rate = 0.01
point = start
val = zval(start[0],start[1])
while True:
    counter += 1
    grad = np.array([dzx(point[0], point[1]), dzy(point[0], point[1])])
    gradmod = float(sp.sqrt(grad[0]*grad[0]+grad[1]*grad[1]))
    oldpoint = point
    oldval = val
    olddif = dif
    dif = decay * dif - rate * grad
    point -= dif
    val = zval(point[0], point[1])
    pointsx.append(copy.copy(point[0]))
    pointsy.append(copy.copy(point[1]))
    difs.append(dif)
    if np.abs(val-oldval) <= thresh and np.abs(np.linalg.norm(point-oldpoint)) <= thresh:
        break
    
print(f'Starting point is ({start[0]},{start[1]})')
print(f'Result is ({point[0].round(5)},{point[1].round(5)})')

def setLinesv2(minx, miny, maxx, maxy):
    delta = 0.0005
    x = np.arange(minx, maxx, delta)
    y = np.arange(miny, maxy, delta)
    X, Y = np.meshgrid(x, y)
    Z = X*Y*(6-X-Y)
    fig, ax = plt.subplots()
    CS = ax.contourf(X, Y, Z, 10, cmap = 'plasma')
    ax.set_title('Gradient descent')
setLinesv2(np.min(pointsx)-0.1, np.min(pointsy)-0.1, np.max(pointsx)+0.1, np.max(pointsy)+0.1)
plt.scatter(pointsx, pointsy, s=2, color='k')

plt.savefig("CalcT62.png")