#Co masz zrobić

#Napisz program, który:



#dla każdej próbki liczy: średnią minimum maksimum wariancję odchylenie standardowe błąd względem 0.5 rysuje histogram dla każdej próbki,
#na końcu wypisuje własny krótki wniosek w print().


import numpy as np
import matplotlib.pyplot as plt

#ustawia seed = 42
np.random.seed(42)

#losuje próbki o rozmiarze:
#50
#500
#5000

sample_sizes = [50, 500, 5000]
for x in sample_sizes:
    sampling=np.random.rand(x)
    mean=np.mean(sampling)
    min=np.min(sampling)
    max=np.max(sampling)
    var=np.var(sampling)
    std=np.std(sampling)
    error=abs(0.5-mean)


    print(f"For amount of samples {x}")
    print(f"Srednia= {mean}")
    print(f"Min= {min}")
    print(f"Max= {max}")
    print(f"Variance= {var}")
    print(f"Standard deviation= {std}")
    print(f"Error= {error}")
    print(f"\n \n ---------------------------------------------")

    plt.hist(sampling, bins=10)
    plt.title(f"Rozkład dla {x} prób")
    plt.ylabel("Ilość prób")
    plt.xlabel("Wartości")
    plt.show()


    #Dla wartości wyższych histogram jest bardziej równomierny, a warość średniej bardziej zbliżona do wartości przewidywanej. Dla wszystkich prypadków wartości std i var są zbliżone