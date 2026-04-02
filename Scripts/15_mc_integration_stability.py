import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

sample_sizes = [100, 1000, 10000, 100000]
a = 0
b = 1
exact_value = 1 / 3

estimates = []
errors = []

for n in sample_sizes:
    x = np.random.uniform(a, b, n)
    y = x**2

    integral_estimate = (b - a) * np.mean(y)
    error = abs(exact_value - integral_estimate)

    estimates.append(integral_estimate)
    errors.append(error)

    print(f"\nLiczba prób: {n}")
    print(f"Estymacja całki: {integral_estimate}")
    print(f"Błąd: {error}")

plt.plot(sample_sizes, estimates, marker='o')
plt.axhline(exact_value)
plt.xscale("log")
plt.xlabel("Liczba prób")
plt.ylabel("Estymacja całki")
plt.title("Stabilizacja całkowania Monte Carlo")
plt.show()