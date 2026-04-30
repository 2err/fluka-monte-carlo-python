import numpy as np
import matplotlib.pyplot as plt


n_particles = 1000
p_absorption = 0.25
thicknesses = [1, 3, 5, 8, 12]
num_experiments = 20


#Średnie wartości po 20 dla kolejnych warstw
#absorbed_num_ex = []
#absorbed_num_ex_dev = []
transmitted_num_ex = []
transmitted_num_ex_dev = []



for thickness in thicknesses:

    trans_part = []
    transmision_1exp = []
    abs_part = []

    for _ in range(num_experiments):

        absorbed = 0
        transmitted = 0
        for n in range(n_particles):
            survived = True
            for _ in range(thickness):
                x=np.random.rand()
                if x<p_absorption:
                    survived=False
                    break

            if survived:
                transmitted+=1

            else:
                absorbed+=1

        trans_part.append(transmitted)
        transmision_1exp.append(transmitted / n_particles)
        abs_part.append(absorbed)

    #print(transmision_1exp)
    transmitted_num_ex.append(float(np.mean(transmision_1exp)))
    transmitted_num_ex_dev.append(float(np.std(transmision_1exp)))


plt.figure(figsize=(8,5))
plt.scatter(thicknesses, transmitted_num_ex, marker="o", color="red")
plt.errorbar(thicknesses, transmitted_num_ex, yerr=transmitted_num_ex_dev, color= "red", fmt='o', ecolor='black', capsize=5)
plt.xlabel("Ilość warstw materiału")
plt.ylabel("Wartość transmisji")
plt.title("Estymacja wartości transmisji ")
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.legend()
plt.savefig("grubość a absorpcja.png", dpi=200, bbox_inches="tight")
plt.show()



for n in thicknesses:
    indeks=thicknesses.index(n)
    print(f"Dla {n} warstw transmisja wynosi {transmitted_num_ex[indeks]}+/-{transmitted_num_ex_dev[indeks]}")

print("Wraz ze wzrostem liczby warstw materiału średnia transmisja maleje. Odchylenie standardowe pokazuje, że między kolejnymi uruchomieniami występuje niewielki rozrzut wyników, ale główny trend pozostaje wyraźny. Oznacza to, że grubszy materiał działa jako skuteczniejsza osłona i przepuszcza coraz mniejszą część wiązki.")





