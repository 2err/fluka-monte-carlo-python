import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n_particles = 1000
p_absorption = 0.3
thicknesses = [1, 3, 5, 8, 12]

transmission_fraction = []
absorption_fraction = []

for thickness in thicknesses:
    absorbed = 0
    transmitted = 0

    for _ in range(n_particles):
        survived = True

        for _ in range(thickness):
            r = np.random.rand()
            if r < p_absorption:
                survived = False
                break

        if survived:
            transmitted += 1
        else:
            absorbed += 1

    transmission_fraction.append(transmitted / n_particles)
    absorption_fraction.append(absorbed / n_particles)

plt.figure(figsize=(8, 5))
plt.plot(thicknesses, transmission_fraction, marker="o", label="Transmisja")
plt.plot(thicknesses, absorption_fraction, marker="o", label="Absorpcja")

plt.xlabel("Grubość materiału (liczba warstw)")
plt.ylabel("Udział cząstek")
plt.title("Wpływ grubości materiału na transmisję i absorpcję")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("transmission_vs_thickness.png", dpi=200, bbox_inches="tight")
plt.show()