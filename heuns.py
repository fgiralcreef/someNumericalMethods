import numpy as np
import matplotlib.pyplot as plt

def heun(x0,y0,f,h,xfinal):
  xs = [x0]
  ys = [y0]
  x = x0
  y = y0
  n = int(round((xfinal-x0)/h))
  for i in range(n):
    k1 = f(x,y)
    prediction = y + h*k1
    k2 = f(x+h,prediction)

    y += h*(k1+k2)/2
    x += h
    
    xs.append(x)
    ys.append(y)
  return xs,ys

a = 0
b = 7
interval = np.linspace(a,b,500)
exact = np.exp(interval)
hache = np.array([1,0.1,0.01,0.001,0.0001])

errores = []
for h in hache:
  xs,ys = heun(a,1,lambda x,y:y,h,7)
  error = abs(ys[-1]-np.exp(7))
  errores.append(error)
  print(h, xs[-1])

  plt.plot(xs,ys,'o-',label="Heuns method")
  plt.plot(interval,exact,label="Exact")
  plt.title("Heuns method and exact solution")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.legend()
  plt.grid()
  plt.show()
errores = np.array(errores)
for i in range(len(errores)-1):
  print(errores[i]/errores[i+1])