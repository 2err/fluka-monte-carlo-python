import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

sample_sizes = [100, 1000, 10000, 100000]
a = 2
b = 4
exact_value = 6

estimates = []
errors = []

for n in sample_sizes:
    x = np.random.uniform(a, b, n)
    y = x

    integral_estimate = (b - a) * np.mean(y)
    error = abs(exact_value - integral_estimate)

    estimates.append(integral_estimate)
    errors.append(error)

    print("**************************************")
    print(f"Estymacja całki dla {n} punktów: {integral_estimate}")
    print(f"Błąd estymacji: {error}")

plt.plot(sample_sizes, estimates, marker='o')
plt.axhline(exact_value)
plt.xscale("log")
plt.xlabel("Liczba punktów")
plt.ylabel("Estymacja całki")
plt.title("Całkowanie Monte Carlo dla f(x)=x")
plt.show()