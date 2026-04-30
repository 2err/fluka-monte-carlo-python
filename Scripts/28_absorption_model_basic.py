import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n_particles = 1000
p_absorption = 0.3

absorbed = 0
transmitted = 0

results = []

for _ in range(n_particles):
    r = np.random.rand()

    if r < p_absorption:
        absorbed += 1
        results.append(0)
    else:
        transmitted += 1
        results.append(1)

transmission = transmitted / n_particles
absorption_fraction = absorbed / n_particles

print("Liczba cząstek:", n_particles)
print("Pochłonięte:", absorbed)
print("Przeszły:", transmitted)
print("Transmisja:", transmission)
print("Udział absorpcji:", absorption_fraction)

plt.hist(results, bins=2)
plt.xticks([0, 1], ["absorbed", "transmitted"])
plt.ylabel("Liczba cząstek")
plt.title("Prosty model absorpcji")
plt.show()