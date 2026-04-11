import numpy as np
import matplotlib.pyplot as plt

np.random.seed(4)

n_particles = 10000
p_absorption = 0.2
thicknesses = [1, 2, 4, 6, 8, 10, 15, 20, 30, 50]

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

    transmission = transmitted / n_particles
    absorption = absorbed / n_particles

    transmission_fraction.append(transmission)
    absorption_fraction.append(absorption)

    print("********************************")
    print(f"Grubość: {thickness}")
    print(f"Transmitowane: {transmitted}")
    print(f"Zaabsorbowane: {absorbed}")
    print(f"Transmisja: {transmission}")
    print(f"Absorpcja: {absorption}")

plt.figure(figsize=(8, 5))
plt.plot(thicknesses, transmission_fraction, marker="o", label="Transmisja")
plt.plot(thicknesses, absorption_fraction, marker="o", label="Absorpcja")

plt.xlabel("Grubość materiału (liczba warstw)")
plt.ylabel("Udział cząstek")
plt.title("Wpływ grubości materiału na transmisję i absorpcję")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()