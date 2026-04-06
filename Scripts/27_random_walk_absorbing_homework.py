import numpy as np
import matplotlib.pyplot as plt

n_particles = 1000

left_boundary = [-5, -10]
right_boundary = [5, 10]

means_steps=[]




for i in range(2):
    left = 0
    right = 0
    all_steps = []
    positions = []
    for n in range(n_particles):
        position=0
        n_step=0
        while left_boundary[i]<position<right_boundary[i]:
            step=np.random.choice([-1, 1])
            n_step+=1
            position+=step
        all_steps.append(n_step)
        positions.append(position)
    mean_n_step=np.mean(all_steps)
    means_steps.append(mean_n_step)
    print(f"Średnia liczba kroków dla granic {left_boundary[i]} i {right_boundary[i]} to {mean_n_step}")

    for item in positions:
        if item>=0:
            right+=1
        elif item<0:
            left+=1

    print(f"Po prawej stronie zatrzymało się {right} cząstek, a po lewej {left}")
    if abs(left-right)<50:
        print(f"Różnica między położeniami po obu stronach mniejsza niż 50 cząstek, cząśtki rozkładają się wmiare równomiernie.")
    else:
        print(f"Cząstki nie rozkładają się równomiernie po obu stronach granic.")

    plt.hist(all_steps, bins=30)
    plt.xlabel("Czas do zatrzymania")
    plt.ylabel("Ilość cząstek")
    plt.title(f"Granice {left_boundary[i]} i {right_boundary[i]}")
    plt.show()

if means_steps[0]<means_steps[1]:
    print(f"Średnio, cząstka zatrzymuje się szybciej przy granicach -5 i 5.")
else:
    print(f"Średnio, cząstka zatrzymuje się szybciej przy granicach -10 i 10.")



