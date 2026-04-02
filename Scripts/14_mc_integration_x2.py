import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 100
a = 0
b = 1

x = np.random.uniform(a, b, n) #Tu losujemy n punktów równomiernie z przedziału [a,b].

y = x**2

integral_estimate = (b - a) * np.mean(y) #Estymacja całki, To średnia wysokość funkcji. (b-a) * np.mean(y) To pole pod wykresem oszacowane metodą Monte Carlo.

exact_value = 1 / 3
error = abs(exact_value - integral_estimate)

print("Liczba prób:", n)
print("Estymacja całki:", integral_estimate)
print("Wartość dokładna:", exact_value)
print("Błąd:", error)

x_plot = np.linspace(a, b, 200)
y_plot = x_plot**2

plt.scatter(x, y, s=2, label="Losowe próbki", color="g")
plt.plot(x_plot, y_plot, label="f(x) = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Całkowanie Monte Carlo dla f(x)=x^2")
plt.legend()
plt.show()
