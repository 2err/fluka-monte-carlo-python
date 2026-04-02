import numpy as np

np.random.seed(42)

n = 10000
exact_value = 0.25

# Zwykłe Monte Carlo
x_uniform = np.random.uniform(0, 1, n)
f_uniform = x_uniform**3
estimate_uniform = np.mean(f_uniform)
error_uniform = abs(exact_value - estimate_uniform)

# Importance sampling
u = np.random.uniform(0, 1, n) #Tu celowo tworzymy rozkład, który częściej daje punkty blisko 1.
x_importance = np.sqrt(u)   # więcej punktów bliżej 1
f_importance = x_importance**3
p_x = 2 * x_importance      # gęstość dla x = sqrt(u)

estimate_importance = np.mean(f_importance / p_x)
error_importance = abs(exact_value - estimate_importance)

print("Dokładna wartość:", exact_value)
print("Zwykłe Monte Carlo:", estimate_uniform)
print("Błąd zwykłego MC:", error_uniform)
print("Importance sampling:", estimate_importance)
print("Błąd importance sampling:", error_importance)