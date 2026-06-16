import numpy as np
import matplotlib.pyplot as plt

def rk4(f,x0,y0,xfinal,h):
  xs = [x0]
  ys = [y0]
  x = x0
  y = y0
  n = int(round((xfinal-x0)/h))
  for _ in range(n):
    k1 = f(x,y)
    k2 = f(x+h/2,y+h*k1/2)
    k3 = f(x+h/2,y+h*k2/2)
    k4 = f(x+h,y+h*k3)
    x += h
    y += (h/6)*(k1+2*k2+2*k3+k4)
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
  xs,ys = rk4(lambda x,y:y,a,1,b,h)
  error = abs(ys[-1]-np.exp(b))
  errores.append(error)
errores = np.array(errores)
print("The ratio of the errors")
for i in range(len(errores)-1):
  print(errores[i]/errores[i+1])

for h,err in zip(hache,errores):
  print(h, err)
plt.loglog(hache,errores,'o-')

plt.title("Error of runge kutta 4")
plt.xlabel("h size")
plt.ylabel("Error")

plt.grid(True, which="both")
plt.show()

