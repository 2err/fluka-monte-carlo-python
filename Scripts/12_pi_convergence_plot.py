import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

sample_sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]
pi_estimates = []

for n in sample_sizes:
    x = np.random.rand(n)
    y = np.random.rand(n)

    inside_circle = x**2 + y**2 <= 1
    points_inside = np.sum(inside_circle)

    pi_estimate = 4 * points_inside / n
    pi_estimates.append(pi_estimate)

plt.plot(sample_sizes, pi_estimates, marker='o')
plt.axhline(np.pi)   #Rysuje poziomą linię na wysokości prawdziwego π
plt.xscale("log") #Skala logarytmiczna pomaga wygodnie pokazać bardzo różne liczby punktów
plt.xlabel("Liczba punktów")
plt.ylabel("Estymacja pi")
plt.title("Stabilizacja estymacji pi")
plt.show()