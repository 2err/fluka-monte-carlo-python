import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n_particles = 1000
left_boundary = -10
right_boundary = 10

steps_to_absorption = []
final_positions = []

for _ in range(n_particles):
    position = 0
    n_steps = 0

    while left_boundary < position < right_boundary:
        step = np.random.choice([-1, 1])
        position += step
        n_steps += 1

    final_positions.append(position)
    steps_to_absorption.append(n_steps)

mean_steps = np.mean(steps_to_absorption)

absorbed_left = final_positions.count(left_boundary)
absorbed_right = final_positions.count(right_boundary)

print("Średnia liczba kroków do zatrzymania:", mean_steps)
print("Liczba cząstek zatrzymanych po lewej:", absorbed_left)
print("Liczba cząstek zatrzymanych po prawej:", absorbed_right)

plt.hist(steps_to_absorption, bins=30)
plt.xlabel("Liczba kroków do zatrzymania")
plt.ylabel("Liczba cząstek")
plt.title("Czas do zatrzymania - random walk 1D")
plt.show()