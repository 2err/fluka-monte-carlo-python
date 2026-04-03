import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n_steps = 100
position = 0    #Startujesz z punktu 0.
positions = [position]

for _ in range(n_steps):
    step = np.random.choice([-1, 1])    #Losujesz krok: w lewo -1 albo w prawo +1
    position += step
    positions.append(position)  #Zapisujesz historię ruchu.

plt.plot(positions)
plt.xlabel("Numer kroku")
plt.ylabel("Pozycja")
plt.title("Random walk 1D")
plt.show()

print("Pozycja końcowa:", position)