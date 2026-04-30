import numpy as np
import matplotlib.pyplot as plt


n_particles=1000
p_absorption=0.3
thicknessess=[1, 3, 5, 8, 12]

absorption=[]
transmission=[]

abs=[]
tra=[]

for thickness in thicknessess:
    absorbed = 0
    transmitted = 0

    for _ in range(n_particles):
        survived = True

        for _ in range(thickness):
            x = np.random.rand()
            if x<p_absorption:
                survived=False
                break

        if survived:
            transmitted += 1

        else:
            absorbed += 1


    absorption.append(float(absorbed))
    abs.append(float(absorbed)/n_particles)
    transmission.append(float(transmitted))
    tra.append(float(transmitted)/n_particles)



print(f"Ilość zaabsorpowanych cząstek: {absorption}")
print(f"Ilość cząstek transmitowanych {transmission}")

plt.plot(thicknessess, tra, marker="o")
plt.xlabel("Grubość materiału")
plt.ylabel("Transmisja")
plt.show()

best_oslona=np.max(absorption)
best_oslona_2=np.min(transmission)
indeks=absorption.index(best_oslona)

print(f"Najlepsza osłona to {thicknessess[indeks]}, dla których absorpcja wynosi {best_oslona} i transmisja {best_oslona_2}")