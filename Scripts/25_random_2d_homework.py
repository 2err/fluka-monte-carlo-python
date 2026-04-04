import numpy as np
import matplotlib.pyplot as plt

n_particles=1000
steps=[10, 100, 1000]

directions=["left", "right", "up", "down"]

x_ended=[]
x_errors=[]
y_ended=[]
y_errors=[]


for n in steps:
    poss_x = []
    poss_y = []
    for _ in range(n_particles):
        position_x=0
        position_y=0

        for n_steps in range(n):
            particle_step=np.random.choice(directions)
            if particle_step=="left":
                position_x-=1
            elif particle_step=="right":
                position_x+=1
            elif particle_step=="up":
                position_y+=1
            else:
                position_y-=1
        poss_x.append(position_x)
        poss_y.append(position_y)


    mean_x=np.mean(poss_x)
    x_ended.append(mean_x)
    std_x=np.std(poss_x)
    x_errors.append(std_x)
    mean_y=np.mean(poss_y)
    y_ended.append(mean_y)
    std_y=np.std(poss_y)
    y_errors.append(std_y)
    print(f"Średnia końcowa wartość x: {mean_x}")
    print(f"Średnia końcowa wartość y: {mean_y}")

    plt.scatter(poss_x, poss_y)
    plt.axis("equal")
    plt.xlabel("Położenie wzglęem x")
    plt.ylabel("Położenie względem y")
    plt.show()

rozrzut_y=np.max(y_errors)
ind_y=y_errors.index(rozrzut_y)
max_roz_y=steps[ind_y]

rozrzut_x=np.max(x_errors)
ind_x=x_errors.index(rozrzut_x)
max_roz_x=steps[ind_x]

print(f"Maksymalna wartość rozrzutu dla wartości y to {rozrzut_y} dla {max_roz_y}.Maksymalna wartość rozrzutu dla wartości y to {rozrzut_x} dla {max_roz_x}.")