#Blackbody spectrum of stars
import numpy as np
import matplotlib.pyplot as plt

def get_spectrum(temp):
    h = 6.626e-34
    c = 3.0e8
    k = 1.38e-23
    
    wavelengths = np.linspace(100e-9, 3000e-9, 500)
    intensity_list = []
    
    for lam in wavelengths:
        top_part = 2 * h * (c**2)
        bottom_part = (lam**5) * (np.exp((h * c) / (lam * k * temp)) - 1)
        
        intensity = top_part / bottom_part
        intensity_list.append(intensity)
        
    return wavelengths, intensity_list

# Comparing stars of two diff temp
w1, i1 = get_spectrum(3000)
w2, i2 = get_spectrum(5000)

plt.plot(w1*1e9, np.array(i1)/1e13, color='red', label="3000K (Red)")
plt.plot(w2*1e9, np.array(i2)/1e13, color='orange', label="5000K (Yellowish)")
plt.ylabel("Intensity (×1e13)")
plt.xlabel("Wavelength (nm)")
plt.legend()
plt.title("The Star's Color changes with Temperature")
plt.show()