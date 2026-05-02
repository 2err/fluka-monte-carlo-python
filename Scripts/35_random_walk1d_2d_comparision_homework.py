import numpy as np
import matplotlib.pyplot as plt

n_particles = 1000
n_steps = 200
steps_list = [50, 200, 1000]

### Przypadek dla 1D

# Porównanie dla różnej liczby kroków
for step in steps_list:
    final_positions_1d = []

    for _ in range(n_particles):
        position = 0
        for _ in range(step):
            x = np.random.choice([-1, 1])
            position += x

        final_positions_1d.append(position)

    mean_1d = np.mean(final_positions_1d)
    std_1d = np.std(final_positions_1d)

    print(f"Dla ruchu w 1D, średnie położenie cząstek dla {step} kroków to {mean_1d}+/- {std_1d}")

    plt.figure(figsize=(8, 5))
    plt.hist(final_positions_1d, bins=30)
    plt.xlabel("Położenie")
    plt.ylabel("Ilość cząstek")
    plt.title(f"Random walk 1D – {step} kroków")
    plt.show()

# Porównanie dla biased
final_positions_sym = []
for _ in range(n_particles):
    position = 0
    for _ in range(n_steps):
        x = np.random.choice([-1, 1])
        position += x
    final_positions_sym.append(position)

mean_sym = np.mean(final_positions_sym)
std_sym = np.std(final_positions_sym)

print(f"Dla ruchu w 1D symetrycznego średnie położenie cząstek to {mean_sym}+/- {std_sym}")

final_positions_biased = []
for _ in range(n_particles):
    position = 0
    for _ in range(n_steps):
        x = np.random.choice([-1, 1], p=[0.4, 0.6])
        position += x
    final_positions_biased.append(position)

mean_biased = np.mean(final_positions_biased)
std_biased = np.std(final_positions_biased)

print(f"Dla ruchu w 1D biased średnie położenie cząstek to {mean_biased}+/- {std_biased}")

plt.figure(figsize=(8, 5))
plt.hist(final_positions_sym, bins=30, alpha=0.6, label="Symetryczny")
plt.hist(final_positions_biased, bins=30, alpha=0.6, label="Biased")
plt.xlabel("Położenie")
plt.ylabel("Ilość cząstek")
plt.legend()
plt.show()

# Granica absorbująca
left = -10
right = 10
left_abs = 0
right_abs = 0
steps_stop = []

for _ in range(n_particles):
    position = 0
    stopst = 0

    while left < position < right:
        x = np.random.choice([-1, 1])
        position += x
        stopst += 1

    if position == left:
        left_abs += 1
    elif position == right:
        right_abs += 1

    steps_stop.append(stopst)

mean_stop = np.mean(steps_stop)

print(f"Przy lewej granicy zatrzymało się {left_abs} cząstek, przy prawej {right_abs} cząstek, a średnia ilość kroków do zatrzymania to {mean_stop}")

### Przypadek dla 2D

final_x = []
final_y = []

for _ in range(n_particles):
    position_x = 0
    position_y = 0

    for _ in range(n_steps):
        step = np.random.choice(["up", "down", "left", "right"])
        if step == "up":
            position_y += 1
        elif step == "down":
            position_y -= 1
        elif step == "left":
            position_x -= 1
        else:
            position_x += 1

    final_x.append(position_x)
    final_y.append(position_y)

mean_x = np.mean(final_x)
std_x = np.std(final_x)
mean_y = np.mean(final_y)
std_y = np.std(final_y)

print(f"W ruchu 2D, średnie położenie w x to {mean_x}+/-{std_x}, a w y to {mean_y}+/-{std_y}")

plt.figure(figsize=(8, 5))
plt.scatter(final_x, final_y, marker='o')
plt.xlabel("Położenie w x")
plt.ylabel("Położenie w y")
plt.axis("equal")
plt.show()