import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n_particles = 1000
left_boundary = -10
right_boundary = 10

steps_to_absorption = []

for _ in range(n_particles):
    position = 0
    n_steps = 0

    while left_boundary < position < right_boundary:
        step = np.random.choice([-1, 1])
        position += step
        n_steps += 1

    steps_to_absorption.append(n_steps)

plt.figure(figsize=(8, 5))
plt.hist(steps_to_absorption, bins=30)

plt.xlabel("Liczba kroków do zatrzymania")
plt.ylabel("Liczba cząstek")
plt.title("Rozkład czasu do zatrzymania w random walk 1D")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()