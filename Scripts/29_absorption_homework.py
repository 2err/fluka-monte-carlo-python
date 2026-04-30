import numpy as np
import matplotlib.pyplot as plt

n_particles=1000

p_abs=[0.2, 0.4, 0.6, 0.8]
transmmision=[]
absorption=[]

for pr_ab in p_abs:
    transmited = 0
    absorbed = 0
    for n in range(n_particles):
        x=np.random.rand()
        if x > pr_ab:
            transmited +=1
        else:
            absorbed +=1
    trans=transmited/n_particles
    transmmision.append(trans)
    print(f"trans={trans}")
    absss=absorbed/n_particles
    absorption.append(absss)
    print(f"abs={absss}")

plt.scatter(p_abs, transmmision, color="red")
plt.xlabel("Prawdopodobieństwo absorpcji")
plt.ylabel("Transmisja")
plt.show()

if transmmision==sorted(transmmision):
    print("Wraz ze wzrostem wartości prawdopodobieństwa absorpcji, rośnie transmisja")
else:
    print("Wraz ze wzrostem wartości prawdopodobieństwa absorpcji, maleje transmisja")

if absorption==sorted(absorption):
    print("Wraz ze wzrostem wartości prawdopodobieństwa absorpcji, rośnie udział absorpcji - materiał bardziej pochłania")
else:
    print("Wraz ze wzrostem wartości prawdopodobieństwa absorpcji, maleje udział absorpcji - materiał mniej pochłania")

