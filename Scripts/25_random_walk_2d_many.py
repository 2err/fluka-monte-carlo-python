import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n_particles = 1000
n_steps = 100

final_x = []
final_y = []

for _ in range(n_particles):
    x, y = 0, 0

    for _ in range(n_steps):
        direction = np.random.choice(["right", "left", "up", "down"])

        if direction == "right":
            x += 1
        elif direction == "left":
            x -= 1
        elif direction == "up":
            y += 1
        elif direction == "down":
            y -= 1

    final_x.append(x)
    final_y.append(y)

mean_x = np.mean(final_x)
mean_y = np.mean(final_y)

print("Średnia końcowa pozycja x:", mean_x)
print("Średnia końcowa pozycja y:", mean_y)

plt.scatter(final_x, final_y, s=10)
plt.xlabel("Końcowe x")
plt.ylabel("Końcowe y")
plt.title("Końcowe pozycje cząstek - random walk 2D")
plt.axis("equal")
plt.show()