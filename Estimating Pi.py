#Estimates the mathematical constant Pi using a Monte Carlo method
import numpy as np
def estimate_pi(n_samples=1000000):
    
    points = np.random.uniform(-1, 1, (n_samples, 2))
    inside_circle = np.sum(np.linalg.norm(points, axis=1) <= 1.0)
    pi_approx = 4 * (inside_circle / n_samples)
    
    print(f"Samples: {n_samples} | Estimated Pi: {pi_approx:.6f}")
    return pi_approx

estimate_pi()