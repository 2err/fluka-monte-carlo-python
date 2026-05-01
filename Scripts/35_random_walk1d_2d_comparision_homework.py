import numpy as np
import matplotlib.pyplot as plt

n_particles = 1000
n_steps = 200

### Przypadek dla 1D

final_positions_1d=[]

for n in range(n_particles):

    position=0
    for _ in range(n_steps):
        x=np.random.choice([-1, 1])
        position+=x

    final_positions_1d.append(position)

mean_1d=np.mean(final_positions_1d)
std_1d=np.std(final_positions_1d)

print(f"Dla ruchu w 1D, średnie położenie cząstek to {mean_1d}+/- {std_1d}")

plt.figure(figsize=(8, 5))
plt.hist(final_positions_1d, bins=30)
plt.xlabel("Położenie")
plt.ylabel("Ilość cząstek")
plt.show()


### Przypadek dla 2D

final_x=[]
final_y=[]

for n in range(n_particles):
    position_x=0
    position_y=0
    for _ in range(n_steps):
        step=np.random.choice(["up", "down", "left", "right"])
        if step=="up":
            position_y+=1
        elif step=="down":
            position_y-=1
        elif step=="left":
            position_x-=1
        else:
            position_x+=1

    final_x.append(position_x)
    final_y.append(position_y)

mean_x=np.mean(final_x)
std_x=np.std(final_x)
mean_y=np.mean(final_y)
std_y=np.std(final_y)

print(f"W ruchu 2D, średnie położenie w x to {mean_x}+/-{std_x}, a w y to {mean_y}+/-{std_y}")

plt.figure(figsize=(8, 5))
plt.scatter(final_x, final_y, marker='o')
plt.xlabel("Położenie w x")
plt.ylabel("Polozenie w y")
plt.show()


