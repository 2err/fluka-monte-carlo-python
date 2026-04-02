import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n = 10000

# granice prostokąta
a, b = 0, 1
c, d = 0, 1

# losowanie punktów (x,y)
x = np.random.uniform(a, b, n)
y = np.random.uniform(c, d, n)

# wartości funkcji f(x,y) = x + y
f_values = x + y

# pole prostokąta
area = (b - a) * (d - c)

# estymacja całki 2D
integral_estimate = area * np.mean(f_values)

# wartość dokładna
exact_value = 1.0
error = abs(exact_value - integral_estimate)

print("Liczba prób:", n)
print("Estymacja całki 2D:", integral_estimate)
print("Wartość dokładna:", exact_value)
print("Błąd:", error)