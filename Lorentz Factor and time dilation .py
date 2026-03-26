#Finding the Lorentz Factor and time dilation
import numpy as np

def calculate_time_dilation(velocity_km_s=250000.0):

    c = 299792.458 # Speed of light in km/s
    beta = velocity_km_s / c
    
    if beta >= 1.0:
        return "Velocity cannot exceed or equal c."

    gamma = 1 / np.sqrt(1 - beta**2)
    
    print(f"Velocity: {velocity_km_s} km/s | Beta: {beta:.4f}")
    print(f"Lorentz Factor (Gamma): {gamma:.6f}")
    print(f"1 hour on spacecraft = {gamma:.2f} hours for an observer at rest.")
    return gamma

calculate_time_dilation(280000.0) # 0.93c
