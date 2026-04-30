import numpy as np
import matplotlib.pyplot as plt

n_particles = 1000
num_experiments = 50
thicknesses = [1, 3, 5, 8, 12]

materials = {
    "A": 0.15,
    "B": 0.30
}

experim_values={"A":[],
                "B":[]}
experim_std={"A":[],
            "B":[]}

for wartosc in materials:
    p_abs = materials[wartosc]



    mean_transmision_thick = []
    std_transmission_thick = []

    for thickness in thicknesses:

        transmission_list=[]
        for _ in range(num_experiments):

            transmited=0
            for _ in range(n_particles):

                survived = True
                for _ in range(thickness):
                    x = np.random.rand()
                    if x<p_abs:
                        survived=False
                        break
                if survived:
                    transmited+=1

            transmission=transmited/n_particles

            #print(transmission)
            transmission_list.append(transmission)

        mean_transmision=np.mean(transmission_list)
        experim_values[wartosc].append(mean_transmision)
        std_transmission=np.std(transmission_list)
        experim_std[wartosc].append(std_transmission)

        #print(experim_values)
        #print(experim_std)

plt.figure(figsize=(8, 5))
for wartosc in experim_values:
    plt.errorbar(thicknesses, experim_values[wartosc], yerr=experim_std[wartosc], marker="o", capsize=5, label=wartosc)

plt.legend()
plt.xlabel("Grubość materiału")
plt.ylabel("Średnia transmisja")
plt.title("Transmisja w funkcji grubości materiału")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

difference=[]
for i in range(len(thicknesses)):
    diff=experim_values["A"][i]-experim_values["B"][i]
    difference.append(abs(diff))

max=np.max(difference)
indeks=difference.index(max)
max_thick=thicknesses[indeks]

print(f"Największa róznica między materiałami występuje dla grubosci {max_thick}, co daje różnice {max}")




