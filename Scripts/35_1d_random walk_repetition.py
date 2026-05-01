import numpy as np
import matplotlib.pyplot as plt

n_particles = 1000
steps_list = [10, 100, 1000]

mean_positions = []
std_positions = []

for n_steps in steps_list:
    final_positions = []

    for _ in range(n_particles):
        position = 0

        for _ in range(n_steps):
            step = np.random.choice([-1, 1])
            position += step

        final_positions.append(position)

    mean_pos = np.mean(final_positions)
    std_pos = np.std(final_positions)

    mean_positions.append(mean_pos)
    std_positions.append(std_pos)

    print(f"Dla {n_steps} kroków:")
    print(f"Średnie położenie = {mean_pos:.4f}")
    print(f"Odchylenie standardowe = {std_pos:.4f}")
    print("----------------------------------")

    plt.figure(figsize=(8, 5))
    plt.hist(final_positions, bins=30)
    plt.xlabel("Końcowe położenie")
    plt.ylabel("Liczba cząstek")
    plt.title(f"Random walk 1D – {n_steps} kroków")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()