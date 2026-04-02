import numpy as np
import matplotlib.pyplot as plt
from matplotlib.bezier import inside_circle
from numpy.ma.core import min_val

# Losujemy punkty w kwadracie o bokach od 0 do 1:
## x z zakresu [0,1)
# y z zakresu [0,1)
#
# Potem sprawdzamy, ile punktów wpada do ćwiartki koła:
# # x² + y² <= 1
#
# Stosunek:
# # punktów w kole do wszystkich punktów pozwala oszacować π.
#
# Bo:#
# pole kwadratu = 1
# pole ćwiartki koła = π/4
#
# pi ≈ 4 * (liczba punktów w kole / liczba wszystkich punktów)

n=200000

x=np.random.rand(n)
y=np.random.rand(n)

circle=x**2 + y**2
inside_circle=circle<=1
points_inside=sum(inside_circle)

pi=4*(points_inside/(n))
pi_solution=np.mean(pi)

print(pi)

# Wykres
plt.figure(figsize=(6, 6))
plt.scatter(x[inside_circle], y[inside_circle], s=1, label="W kole")
plt.scatter(x[~inside_circle], y[~inside_circle], s=1, label="Poza kołem")
plt.title(f"Monte Carlo: estymacja pi = {pi}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.axis("equal")
plt.show()