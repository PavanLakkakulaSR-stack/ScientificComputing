#Calculating the half-life of a substance using its decay constant
import numpy as np

def calculate_half_life(lambda_decay):

    half_life = np.log(2) / lambda_decay
    return half_life

# does it for Cobalt-60
lambda_co60 = 0.131 # per year
print(f"Decay Constant (lambda): {lambda_co60}")
print(f"Calculated Half-life: {calculate_half_life(lambda_co60):.2f} years")
