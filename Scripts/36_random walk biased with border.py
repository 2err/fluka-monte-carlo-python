import numpy as np
import matplotlib.pyplot as plt

n_particles = 1000
steps_list = [50, 200, 1000]

# ---------------------------
# CZĘŚĆ 1: zwykły random walk 1D
# ---------------------------

print("=== CZĘŚĆ 1: wpływ liczby kroków ===")

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

    print(f"{n_steps} kroków -> średnia = {mean_pos:.4f}, std = {std_pos:.4f}")

    plt.figure(figsize=(8, 5))
    plt.hist(final_positions, bins=30)
    plt.xlabel("Końcowe położenie")
    plt.ylabel("Liczba cząstek")
    plt.title(f"Random walk 1D – {n_steps} kroków")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

# ---------------------------
# CZĘŚĆ 2: random walk z biasem
# ---------------------------

print("\n=== CZĘŚĆ 2: bias w prawo ===")

n_steps = 200
final_positions_sym = []
final_positions_bias = []

for _ in range(n_particles):
    # ruch symetryczny
    position = 0
    for _ in range(n_steps):
        step = np.random.choice([-1, 1])
        position += step
    final_positions_sym.append(position)

    # ruch z biasem
    position = 0
    for _ in range(n_steps):
        step = np.random.choice([-1, 1], p=[0.4, 0.6])   # 40% lewo, 60% prawo
        position += step
    final_positions_bias.append(position)

print(f"Symetryczny: średnia = {np.mean(final_positions_sym):.4f}, std = {np.std(final_positions_sym):.4f}")
print(f"Bias w prawo: średnia = {np.mean(final_positions_bias):.4f}, std = {np.std(final_positions_bias):.4f}")

plt.figure(figsize=(8, 5))
plt.hist(final_positions_sym, bins=30, alpha=0.6, label="Symetryczny")
plt.hist(final_positions_bias, bins=30, alpha=0.6, label="Bias w prawo")
plt.xlabel("Końcowe położenie")
plt.ylabel("Liczba cząstek")
plt.title("Porównanie random walk symetrycznego i biased")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ---------------------------
# CZĘŚĆ 3: granice absorbujące
# ---------------------------

print("\n=== CZĘŚĆ 3: granice absorbujące ===")

left_boundary = -10
right_boundary = 10

final_sides = []
steps_to_absorption = []

for _ in range(n_particles):
    position = 0
    n_steps_taken = 0

    while left_boundary < position < right_boundary:
        step = np.random.choice([-1, 1])
        position += step
        n_steps_taken += 1

    final_sides.append(position)
    steps_to_absorption.append(n_steps_taken)

mean_steps = np.mean(steps_to_absorption)
left_count = sum(1 for x in final_sides if x == left_boundary)
right_count = sum(1 for x in final_sides if x == right_boundary)

print(f"Średnia liczba kroków do zatrzymania = {mean_steps:.4f}")
print(f"Lewa granica: {left_count}")
print(f"Prawa granica: {right_count}")

plt.figure(figsize=(8, 5))
plt.hist(steps_to_absorption, bins=30)
plt.xlabel("Liczba kroków do zatrzymania")
plt.ylabel("Liczba cząstek")
plt.title("Random walk 1D z granicami absorbującymi")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()