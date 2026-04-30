import numpy as np
import matplotlib.pyplot as plt

n_particles = 1000
num_experiments = 50
p_absorption = 0.2
thicknesses = [1, 3, 5, 8, 12]

mean_transmissions = []
std_transmissions = []

for thickness in thicknesses:
    experiment_results = []

    for _ in range(num_experiments):
        transmitted = 0

        for _ in range(n_particles):
            survived = True

            for _ in range(thickness):
                x = np.random.rand()
                if x < p_absorption:
                    survived = False
                    break

            if survived:
                transmitted += 1

        transmission = transmitted / n_particles
        experiment_results.append(transmission)

    mean_transmissions.append(np.mean(experiment_results))
    std_transmissions.append(np.std(experiment_results))

for i in range(len(thicknesses)):
    print(f"Grubość {thicknesses[i]}: transmisja = {mean_transmissions[i]:.4f} +/- {std_transmissions[i]:.4f}")

plt.figure(figsize=(8, 5))
plt.errorbar(thicknesses, mean_transmissions, yerr=std_transmissions, marker="o", capsize=5)
plt.xlabel("Grubość materiału")
plt.ylabel("Średnia transmisja")
plt.title("Transmisja w funkcji grubości materiału")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()