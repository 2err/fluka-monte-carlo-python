import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n_steps = 200

x, y = 0, 0
x_positions = [x]
y_positions = [y]

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

    x_positions.append(x)
    y_positions.append(y)

plt.plot(x_positions, y_positions, marker="o", markersize=2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Random walk 2D - jedna trajektoria")
plt.axis("equal")          # dzięki temu oś x i y mają tę samą skalę.Tor nie będzie wizualnie zniekształcony.
plt.show()

print("Końcowa pozycja:", (x, y))