import numpy as np
import matplotlib.pyplot as plt

n_particles = 1000
num_experiments = 50
thicknesses=[1, 3, 5, 8, 12]

materials= {
    "M.1" : 0.15,
    "M.2" : 0.3}

results={}

for material_name, p_absorption in materials.items():
    mean_transmissions = []
    std_transmissions = []
    for thickness in thicknesses:

        absorbed=0
        transmission = []
        for _ in range(num_experiments):
            transmited = 0
            for _ in range(n_particles):
                survived = True

                for _ in range(thickness):
                    x = np.random.rand()
                    if x<p_absorption:
                        survived=False
                        break
                if survived==True:
                    transmited+=1
                #else:
                #    absorbed+=1
            print(transmited)
            tran_part=transmited/n_particles
            transmission.append(tran_part)

        mean_transmissions.append(float(np.mean(transmission)))
        std_transmissions.append(float(np.std(transmission)))



    results[material_name]={"mean":mean_transmissions, "std":std_transmissions}

print(results)

for material_name in materials.keys():
    plt.errorbar(thicknesses, results[material_name]["mean"], yerr=results[material_name]["std"], marker="o", label=material_name)
plt.xlabel("Grubość materiału (liczba warstw)")
plt.ylabel("Średnia transmisja")
plt.title("Porównanie transmisji dla dwóch materiałów")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()