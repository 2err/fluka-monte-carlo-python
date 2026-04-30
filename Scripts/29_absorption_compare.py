import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n_particles = 1000
absorption_probs = [0.1, 0.3, 0.6]

transmissions = []
absorptions = []

for p_absorption in absorption_probs:
    absorbed = 0
    transmitted = 0

    for _ in range(n_particles):
        r = np.random.rand()

        if r < p_absorption:
            absorbed += 1
        else:
            transmitted += 1

    transmission = transmitted / n_particles
    absorption_fraction = absorbed / n_particles

    transmissions.append(transmission)
    absorptions.append(absorption_fraction)

    print("************************************")
    print(f"Prawdopodobieństwo absorpcji: {p_absorption}")
    print(f"Pochłonięte: {absorbed}")
    print(f"Przeszły: {transmitted}")
    print(f"Transmisja: {transmission}")
    print(f"Udział absorpcji: {absorption_fraction}")

plt.plot(absorption_probs, transmissions, marker="o", label="Transmisja")
plt.plot(absorption_probs, absorptions, marker="o", label="Absorpcja")
plt.xlabel("Prawdopodobieństwo absorpcji")
plt.ylabel("Udział")
plt.title("Porównanie transmisji i absorpcji")
plt.legend()
plt.show()