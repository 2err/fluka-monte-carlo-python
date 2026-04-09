import numpy as np
import matplotlib.pyplot as plt

a=0
b=1
exact_value=0.25

sample_size=[100, 1000, 10000, 100000]
integrals=[]

for n in sample_size:
    x=np.random.uniform(0,1, n)
    y=x**3

    integral=(b-a)*np.mean(y)
    integrals.append(integral)

plt.figure(figsize=(8,5))
plt.plot(sample_size, integrals, marker="o", color="blue", alpha=0.7)
plt.axhline(exact_value, color="red", alpha=0.4)
plt.xscale("log")
plt.xlabel("Liczba próbek")
plt.ylabel("Estymacja wartości całki")
plt.title("Estymacja całki ∫₀¹ x³ dx metodą Monte Carlo")
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.legend()
plt.savefig("estymacja_calki.png", dpi=200, bbox_inches="tight")
plt.show()


