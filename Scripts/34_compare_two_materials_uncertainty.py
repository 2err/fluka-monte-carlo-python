import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n_particles = 1000
num_experiments = 20
thicknesses = [1, 3, 5, 8, 12]

materials = {
    "Materiał A": 0.20,
    "Materiał B": 0.35
}

results = {}

for material_name, p_absorption in materials.items():
    mean_transmissions = []
    std_transmissions = []

    for thickness in thicknesses:
        transmission_results = []

        for _ in range(num_experiments):
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

            transmission = transmitted / n_particles
            transmission_results.append(transmission)

        mean_t = np.mean(transmission_results)
        std_t = np.std(transmission_results)

        mean_transmissions.append(mean_t)
        std_transmissions.append(std_t)

        print("**************************************")
        print(f"{material_name}, grubość {thickness}")
        print(f"Średnia transmisja: {mean_t}")
        print(f"Odchylenie standardowe: {std_t}")

    results[material_name] = {
        "mean": mean_transmissions,
        "std": std_transmissions
    }

plt.figure(figsize=(8, 5))

for material_name in materials.keys():
    plt.errorbar(
        thicknesses,
        results[material_name]["mean"],
        yerr=results[material_name]["std"],
        marker="o",
        capsize=4,
        label=material_name
    )

plt.xlabel("Grubość materiału (liczba warstw)")
plt.ylabel("Średnia transmisja")
plt.title("Porównanie transmisji dla dwóch materiałów")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()