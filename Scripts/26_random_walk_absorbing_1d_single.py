import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

#Granice - ściany absorbujące
left_boundary = -10
right_boundary = 10

position = 0
positions = [position]
n_steps = 0

while left_boundary < position < right_boundary: #Dopóki cząstka jest między granicami, idzie dalej
    step = np.random.choice([-1, 1])
    position += step
    positions.append(position)
    n_steps += 1

plt.plot(positions, marker="o", markersize=3)
plt.axhline(left_boundary)
plt.axhline(right_boundary)
plt.xlabel("Numer kroku")
plt.ylabel("Pozycja")
plt.title("Random walk 1D z zatrzymaniem")
plt.show()

print("Końcowa pozycja:", position)
print("Liczba kroków do zatrzymania:", n_steps)
