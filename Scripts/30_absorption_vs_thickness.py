import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n_particles = 1000
p_absorption = 0.2
thicknesses = [1, 2, 5, 10]

transmissions = []
absorptions = []

for thickness in thicknesses: #Badamy różne grubości materiału.
    transmitted = 0
    absorbed = 0

    for _ in range(n_particles):
        survived = True

        for _ in range(thickness): #To są kolejne warstwy materiału.
            r = np.random.rand()

            if r < p_absorption: #Na każdej warstwie cząstka może zostać pochłonięta.
                survived = False
                break #Jeśli już została pochłonięta, nie idzie dalej przez następne warstwy.

        if survived:
            transmitted += 1
        else:
            absorbed += 1

    transmission = transmitted / n_particles
    absorption_fraction = absorbed / n_particles

    transmissions.append(transmission)
    absorptions.append(absorption_fraction)

    print("************************************")
    print(f"Grubość materiału: {thickness}")
    print(f"Pochłonięte: {absorbed}")
    print(f"Przeszły: {transmitted}")
    print(f"Transmisja: {transmission}")
    print(f"Udział absorpcji: {absorption_fraction}")

plt.plot(thicknesses, transmissions, marker="o", label="Transmisja")
plt.plot(thicknesses, absorptions, marker="o", label="Absorpcja")
plt.xlabel("Grubość materiału (liczba warstw)")
plt.ylabel("Udział")
plt.title("Wpływ grubości materiału na transmisję")
plt.legend()
plt.show()