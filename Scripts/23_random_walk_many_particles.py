import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n_particles = 1000
n_steps = 100

final_positions = []

for _ in range(n_particles):
    position = 0

    for _ in range(n_steps):
        step = np.random.choice([-1, 1])
        position += step

    final_positions.append(position)

mean_position = np.mean(final_positions)
std_position = np.std(final_positions)

print("Średnia końcowa pozycja:", mean_position)
print("Odchylenie standardowe:", std_position)

plt.hist(final_positions, bins=30)
plt.xlabel("Końcowa pozycja")
plt.ylabel("Liczba cząstek")
plt.title("Histogram końcowych pozycji - random walk 1D")
plt.show()