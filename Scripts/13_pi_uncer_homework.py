import numpy as np
import matplotlib.pyplot as plt

sample_sizes = [1000, 10000]
estimates = 20


mean_pi=[]
std_pi=[]
min_pi=[]
max_pi=[]
error_pi=[]

for n in sample_sizes:
    pi_estim = []
    for i in range(estimates):
        x=np.random.rand(n)
        y=np.random.rand(n)

        inside_circle=x**2+y**2<=1
        pi_e=4*(np.sum(inside_circle)/n)

        pi_estim.append(pi_e)

    meanpi=np.mean(pi_estim)
    mean_pi.append(meanpi)
    print(f"---------------------------------------\n")
    print(f"Dla {n} póbek średnia wartość pi wynosi {meanpi}")
    stdpi=np.std(pi_estim)
    std_pi.append(stdpi)
    print(f"Dla {n} póbek odchylenie standardowe pi wynosi {stdpi}")
    minpi = np.min(pi_estim)
    min_pi.append(minpi)
    print(f"Dla {n} póbek minimalna wartość pi wynosi {minpi}")
    maxpi = np.max(pi_estim)
    max_pi.append(maxpi)
    print(f"Dla {n} póbek maksymalna wartość pi wynosi {maxpi}")
    errorpi = abs(meanpi-np.pi)
    error_pi.append(errorpi)
    print(f"Dla {n} póbek błąd estymacji pi wynosi {errorpi}")

    plt.hist(pi_estim, bins=30)
    plt.ylabel("ilość powtórzeń")
    plt.xlabel("wartość")
    plt.title(f"Wartość oszacowana dla próbek {n}")
    plt.show()


best_error=float(np.min(error_pi))
indeks=error_pi.index(best_error)

print(f"_____________________________________________________\n")
print(f"Dla analizowanych wyników najlepsze oszacowanie to {mean_pi[indeks]}+/-{std_pi[indeks]}, dla któego błąd estymacji wynosi {best_error}. Aby uzyskać taki wynik nalezalo wygenerować {sample_sizes[indeks]} prób.")



