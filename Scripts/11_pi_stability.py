import numpy as np

np.random.seed(42)

sample_sizes = [100, 1000, 10000, 100000]

for n in sample_sizes:
    x = np.random.rand(n)
    y = np.random.rand(n)

    inside_circle = x**2 + y**2 <= 1
    points_inside = np.sum(inside_circle)

    pi_estimate = 4 * points_inside / n
    error = abs(np.pi - pi_estimate)

    print(f"\nLiczba punktów: {n}")
    print(f"Estymacja pi: {pi_estimate}")
    print(f"Błąd: {error}")