#Simulating a 1D chain of magnetic spins using the Metropolis algorithm to show how energy and entropy compete
import numpy as np
import matplotlib.pyplot as plt
import random

def run_spin_simulation(): 
    num_spins = 100
    temp = 0.5
    spins = []
    for i in range(num_spins):
        spins.append(random.choice([-1, 1]))

    for step in range(5000):
        i = random.randint(0, num_spins - 1)
        left = spins[i-1]
        right = spins[(i+1) % num_spins]
        current_energy = -1 * spins[i] * (left + right)
        flipped_energy = -1 * (-spins[i]) * (left + right)
        
        energy_change = flipped_energy - current_energy
        if energy_change <= 0:
            spins[i] = -spins[i]
        else:
            prob = np.exp(-energy_change / temp)
            if random.random() < prob:
                spins[i] = -spins[i]

    #Plotiing
    plt.plot(spins, 'b-')
    plt.title("Magnetic Domains forming at Low Temp")
    plt.show()

run_spin_simulation()