#Heisenberg position momentum uncertainty simulation
import numpy as np
import matplotlib.pyplot as plt

def show_uncertainty():
    x_axis = np.linspace(-10, 10, 1000)
    width = 0.2 
    # Using Gaussian formula
    position_wave = np.exp(-(x_axis**2) / (2 * width**2))
    momentum_wave = np.fft.fft(position_wave)
    momentum_real = np.abs(momentum_wave)
    
    #Plotting
    #shows position
    plt.subplot(2, 1, 1)
    plt.plot(x_axis, position_wave)
    plt.title("Narrow Position")
    #shows momentum
    plt.subplot(2, 1, 2)
    # shows only part of momentum (not centered)
    plt.plot(momentum_real[:100])
    plt.title("Wide Momentum")
    plt.tight_layout()
    plt.show()

show_uncertainty()