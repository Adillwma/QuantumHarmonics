### - Loading Dependencies
import numpy as np
from scipy.linalg import eigh_tridiagonal     # Used to solve for eigenvalue and eigenvectors (Compared various routines)
from helper_functions import generate_x

# Potential Energy Function for Quantum Harmonic Oscillator
def potential_qho(x):
    """
    Input: x: Discrete spatial x values as N x 1 array.
    
    Returns: v: N x 1 array with the corresponsing potential energy of the QHO at each x value.
    """
    v = x**2       #Quantum Harmonic Oscillator Potential Energy
    return v

# Hamiltonian tridiag Function                      
def hamiltonian_diag(x, V, delta_x):

    """
    The following function, given the discrete space points $x_i$ and the potential $V_i$, constructs and returns the Hamiltonian matrix.

    Input: x: Discrete x values as N x 1 array, 
           V: Potential Energy values as N x 1 array, 
           delta_x: The step size (dx) as a single float
    
    Returns: H_main: Hamiltonian leading diagonal as 1D array, 
             H_plusone: Hamiltonian ofset diagonal as 1D array.
    """
    #The kinetic energy term of the Hamiltonian  
    D_main = np.full(len(x), fill_value = 2/(delta_x**2))           #Creates a 1D array of same length of x where each value is 2/(delta_x**2
    D_plusone = np.full(len(x) - 1 , fill_value = -1/(delta_x**2))    #Creates a 1D array of same length of x-1 (Ofset diagonals length is 1 less than on the leading diagonal), where each vlue is -1/(delta_x**2)

    #The Hamiltonian matrix, 𝐻=𝐷+𝑉                                #V is not calculated in function as it is passed n as argument already in the correct 1D format
    H_main = D_main + V                                           #Creates the 1D hamiltonain leading diagonal by combining the Kinetic and Potential energy arrays leading diagonals values
    H_plusone = D_plusone                                         #Creates the 1D hamiltonain ofset diagonal by combining th Kinetic and Potential energy arrays ofset diagonals values (Potential energy ofset diagonalas are all 0 so just the Kinetic energy term is used)
    
    return(H_main, H_plusone)                                     #Returns the Hamiltonian 1D leading diagonal and the Hamiltonian 1D offset diagonal

### - Function for QHO - (Now with the testing done clean function for the whole QHO calculation without all the testing loops and analytical checking etc, and only using the prefered scipy solver, eigh.tridiag)
def QHO_simulation(x, delta_x, maxE_val, minE_val= 0):
    """
    Input: 
            N: Int value for number of points to divide the spatial range into, 
            maxE_val: maximum desired eigenvalue, 
    
    Returns:
            x: Discrete x values as N x 1 array, 
            delta_x: The step size (dx) as a single float,
            N: Int value for number of points to divide the spatial range into,
            V_qho:, Potential Energy values as N x 1 array,
            E_vals_tridiag: List of numerically calculated eigenvalues, 
            E_vectors_tridiag List of numerically calculated eigenvectors
    """  
    V_qho = potential_qho(x)                                                     #QHO potential function
    H_main, H_plusone = hamiltonian_diag(x, V_qho, delta_x)                      #Hamiltonian function
                                                                            #If user specifies both a minimum and maximum eigenvalue, only eigenvalues within this range are calculated
    E_vals_tridiag, E_vectors_tridiag = eigh_tridiagonal(H_main, H_plusone, select="i", select_range=(minE_val, maxE_val))
    E_vectors_tridiag = E_vectors_tridiag / np.sqrt(delta_x)                    #Normalising the eigenvectors


    print("E VAL LENGTH", len(E_vals_tridiag))
    print("E VECTORS LENGTH", len(E_vectors_tridiag))

    p_densitys = E_vectors_tridiag**2

    return V_qho, E_vals_tridiag, E_vectors_tridiag, p_densitys              #Returns all calulated values and steps for further processing or visulisation


if __name__ == "__main__":
        
    # User Settings
    max_n = 10
    
    N = 100 
    x_min = -5
    x_max = 5

    x, delta_x = generate_x(x_min, x_max, N)                           #Spatial Discretisation  function 
    V_qho, E_vals_tridiag, E_vectors_tridiag, p_densitys = QHO_simulation(x, delta_x, max_n)


