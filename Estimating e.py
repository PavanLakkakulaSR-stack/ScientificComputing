  #Estimating the mathematical constant e
    
import numpy as np

def estimate_euler_number(n=1000000):
    
    e_approx = (1 + 1/n)**n
    
    # Finding error
    true_e = np.e
    error = abs(true_e - e_approx)
    
    print(f"n: {n} | Estimated e: {e_approx:.10f}")
    print(f"True e: {true_e:.10f} | Absolute Error: {error:.2e}")
    return e_approx

estimate_euler_number()