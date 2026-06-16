import numpy as np
import matplotlib.pyplot as plt

def euler(x0,y0,fprime,h,xfinal):
  xs = [x0]
  ys = [y0]
  x = x0
  y = y0
  while x < xfinal:
    y = y + h*fprime(x,y)
    x+=h
    xs.append(x)
    ys.append(y)
  return xs,ys

a = 0
b = 1
iv = 1
interval = np.linspace(a,b,500)
exact = np.exp(interval)

hache = np.array([1,0.1,0.01,0.001,0.0001])

errores = []
for h in hache:
  xs,ys = euler(a,iv,lambda x,y:y,h,b)
  error = abs(ys[-1]-np.exp(1))
  errores.append(error)
  plt.plot(xs,ys,'o-',label="Euler")
  plt.plot(interval,exact,label="Exact")
 
  plt.title(f"Eulers method vs exact solution with h as: {h}")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.legend()
  plt.grid()
  plt.show()
errores = np.array(errores)

plt.loglog(hache,errores,'o-')
plt.title("Error in eulers method as h changes")
plt.xlabel("h")
plt.ylabel("Error")
plt.grid()
plt.show()

for i in range(len(errores)-1):
  print(errores[i]/errores[i+1])
for hval, err in zip(hache, errores):
    print(err/hval)