import numpy as np

np.random.seed(42)

n = 5000
num_experiments = 20
exact_value = 0.25

uniform_results = []
importance_results = []

for _ in range(num_experiments):
    # zwykłe MC
    x_uniform = np.random.uniform(0, 1, n)
    estimate_uniform = np.mean(x_uniform**3)
    uniform_results.append(estimate_uniform)

    # importance sampling
    u = np.random.uniform(0, 1, n)
    x_importance = np.sqrt(u)
    p_x = 2 * x_importance
    estimate_importance = np.mean((x_importance**3) / p_x)
    importance_results.append(estimate_importance)

mean_uniform = np.mean(uniform_results)
std_uniform = np.std(uniform_results)

mean_importance = np.mean(importance_results)
std_importance = np.std(importance_results)

print("Dokładna wartość:", exact_value)
print("\nZwykłe Monte Carlo")
print("Średnia:", mean_uniform)
print("Odchylenie standardowe:", std_uniform)
print("Błąd średniej:", abs(exact_value - mean_uniform))

print("\nImportance sampling")
print("Średnia:", mean_importance)
print("Odchylenie standardowe:", std_importance)
print("Błąd średniej:", abs(exact_value - mean_importance))