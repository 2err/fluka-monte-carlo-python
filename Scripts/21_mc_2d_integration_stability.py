import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

sample_sizes = [100, 1000, 10000, 100000]

a, b = 0, 1
c, d = 0, 1
area = (b - a) * (d - c)
exact_value = 1.0

estimates = []
errors = []

for n in sample_sizes:
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(c, d, n)

    f_values = x + y
    integral_estimate = area * np.mean(f_values)
    error = abs(exact_value - integral_estimate)

    estimates.append(integral_estimate)
    errors.append(error)

    print("**************************************")
    print(f"Liczba prób: {n}")
    print(f"Estymacja całki 2D: {integral_estimate}")
    print(f"Błąd: {error}")

plt.plot(sample_sizes, estimates, marker="o")
plt.axhline(exact_value)
plt.xscale("log")
plt.xlabel("Liczba prób")
plt.ylabel("Estymacja całki 2D")
plt.title("Stabilizacja całkowania Monte Carlo 2D")
plt.show()