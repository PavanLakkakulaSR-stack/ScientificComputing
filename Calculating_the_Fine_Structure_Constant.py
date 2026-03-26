 #Calculates the Fine Structure Constant
    
import numpy as np

def calculate_fine_structure():
   
    e = 1.602176634e-19  # Elementary charge
    hbar = 1.054571817e-34 # Reduced Planck constant
    c = 299792458         # Speed of light
    epsilon_0 = 8.8541878128e-12 # Vacuum permittivity
    
    alpha = (e**2) / (4 * np.pi * epsilon_0 * hbar * c)
    
    print(f"Alpha (Fine-Structure Constant): {alpha:.8f}")
    print(f"Approximated value: 1/{1/alpha:.2f}")
    return alpha

calculate_fine_structure()
