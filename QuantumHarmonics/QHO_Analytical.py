
import numpy as np
from mpmath import factorial
from helper_functions import generate_x




### - Analytical Quantum Harmonic Oscillator Eigenvalues
def qho_analytical_e_values(max_n, min_n=1):
    """
    Input: maxE_val: maximum desired eigenvalue
    
    Returns: analytical_E_vals: 1D list of analytical eigenvales for the QHO from ground state up till maxE_val
             n_vals: 1D list of index positions for the analytical eigenvales
    """    
    print(max_n)
    n_vals = np.arange(min_n, max_n + 1, 1)                #Initialises list to hold the index values for the analytical eignevalues
    analytical_E_vals = 2 * n_vals + 1             #Calculates the analytical eigenvalues, which are given by (n*2)+1 due to the choice of units we have used for energy (1/2)*ℏ𝜔

    return(analytical_E_vals, n_vals)              #Returns the list of eigenvalues and the list of index values

### - Analytical Quantum Harmonic Oscillator Eigenvectors
def qho_analytical_e_vectors(x, max_n, min_n=1):

    wavefunctions = []

    for n in range(min_n, max_n+1):

        if n <= 150:
            prefactor = (1 / np.sqrt(2**n * np.math.factorial(n) * np.sqrt(np.pi)))
        else:
            prefactor = (1 / np.sqrt(2**n * factorial(n) * np.sqrt(np.pi)))
            prefactor = np.array(prefactor, dtype=np.float64)

        hermite = np.polynomial.hermite.Hermite([0]*n + [1])(x)  # Calculate the Hermite polynomial of order n
        gaussian = np.exp(-x**2 / 2)  # Gaussian function
        term = prefactor * hermite * gaussian  # Multiply Hermite polynomial by Gaussian
        wavefunctions.append(term)


    return np.array(wavefunctions)

def QHO_analytical_soloution(x, max_n, min_n=1):
    E_vals, n_vals = qho_analytical_e_values(max_n, min_n)
    wavefunctions = qho_analytical_e_vectors(x, max_n-1, min_n-1)     # fix the n-1 positioning

    return n_vals, E_vals, wavefunctions


if __name__ == "__main__":
        
    # User Settings    
    min_n = 1
    max_n = 1000
    
    x_min = -5
    x_max = 5
    N = 1000 

    x, delta_x = generate_x(x_min, x_max, N)                           #Spatial Discretisation
    n_vals, E_vals, wavefunctions = QHO_analytical_soloution(x, max_n, min_n)
    