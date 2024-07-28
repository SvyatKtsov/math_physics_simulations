import sys
import os

paths_of_all_libs = os.path.abspath('d:/random_py_projects/lib/site-packages')
if paths_of_all_libs not in sys.path:
    sys.path.insert(0, paths_of_all_libs)



import sympy as sp
import numpy as np
import matplotlib.pyplot as plt



x, t, n = sp.symbols('x t n', real=True)
L = 4.526  # 
K = 8.23544  #=

#   initial temperature distribution function f(x)
f = lambda x: sp.sin(np.pi * x / L)  


N = 9 


An = (2/L) * sp.integrate(f(x) * sp.sin((n *np.pi *x)/ L), (x, 0, L))

u = 0
for i in range(1, N + 1):
    u += An.subs(n, i) * sp.sin((i * np.pi * x)/ L) * sp.exp(-K*i**2 * np.pi**2 *t / L**2)


u = sp.simplify(u)

spatial_ = np.linspace(0, L, 120)  #  120 points between 0 and L for x
t_ = np.linspace(0, 35, 35)  # time points


X, T = np.meshgrid(spatial_, t_)
temperature = np.zeros_like(X, dtype=float)


for i in range(len(t_)):
    for j in range(len(spatial_)):
        temperature[i, j] = float(u.subs({x: spatial_[j], t: t_[i]}).evalf())

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(T, X, temperature, cmap='viridis')

ax.set_xlabel('Time from start')
ax.set_ylabel('Position on the rod (x)')
ax.set_zlabel('Temperature')
ax.set_title('Temperature Distribution over Time and Space')

plt.show()
