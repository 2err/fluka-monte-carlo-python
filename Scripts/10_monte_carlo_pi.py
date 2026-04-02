import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 200000

x = np.random.rand(n)
y = np.random.rand(n)

inside_circle = x**2 + y**2 <= 1  #To daje tablicę wartości logicznych: True dla punktów w kole, False dla punktów poza kołem.

points_inside = np.sum(inside_circle)
pi_estimate = 4 * points_inside / n
error = abs(np.pi - pi_estimate)

print("Liczba punktów:", n)
print("Punkty w kole:", points_inside)
print("Estymacja pi:", pi_estimate)
print("Błąd:", error)


plt.figure(figsize=(6, 6))
plt.scatter(x[inside_circle], y[inside_circle], s=1, label="W kole")
plt.scatter(x[~inside_circle], y[~inside_circle], s=1, label="Poza kołem") #Co robi ~inside_circle? jeśli inside_circle jest True, to ~inside_circle daje False,i odwrotnie.
plt.title(f"Monte Carlo: estymacja pi = {pi_estimate}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.axis("equal")
plt.show()