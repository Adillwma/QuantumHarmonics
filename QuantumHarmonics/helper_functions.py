from matplotlib import pyplot as plt
import numpy as np

### - Helper Functions

#Plotting Function - Just to tidy up the repeated use of plotting and allows for ease of use of symetric function and creating quick subplots    
def SimplePlotAssist(xvals, yvals, title='title', xlabel='xlabel (Units)', ylabel='ylabel (Units)', colour='b', ax_mode=0, symetrical=0):
    """
    Inputs: x, y, title, xlabel, ylabel, colour, ax_mode (selecting '0' uses 'plt.', '1' uses 'ax.'), 
            symetrical (setting to 1 will symetrise y limits around y=0) 
    
    Returns: matplotlib plot not yet printed. Can be imidietly printed after function call with 
             plt.show() or can be put into subplots by calling plt.subplot(rows,columns,index) 
             before function call.
    """    

    if ax_mode == 0:
        plt.plot(xvals,yvals)          #Plots Xn against Yn
        plt.title(title)               #Gives the individual subplot a title
        plt.xlabel(xlabel)             #X axis label for this subplot
        plt.ylabel(ylabel)             #Y axis label for this subplot

    else:
        ax.plot(xvals,yvals, c=colour)                     #Plots Xn against Yn
        ax.set_title(title)                                #Gives the individual subplot a title
        ax.set_xlabel(xlabel)                              #X axis label for this subplot        
        ax.set_ylabel(ylabel)                              #Y axis label for this subplot
        if symetrical == 1:                                #Checks if user requested the symetrical argument 
            y_max = np.abs(ax.get_ylim()).max()            #Finds maximum absoloute amplitude
            ax.set_ylim(ymin= -y_max, ymax= y_max)         #Sets y limits to max abs amplitude and its negative, centring plot on 0     

def find_local_maxima(array):
    indicies = []
    values = []
    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            indicies.append(i)
            values.append(array[i])

    return indicies, values

def bohr_radius_to_angstrom(bohr_radius):
    """
    Bohr Radius (a₀): It's a physical constant representing the most probable distance between the nucleus and the electron in a hydrogen atom when it's in its ground state. It's approximately equal to 0.529177 angstroms.
    Angstrom (Å): It's a unit of length used to measure very small distances, primarily in atomic-scale physics and chemistry. 1 angstrom is equal to 0.1 nanometers or 10−1010−10 meters. It's commonly used to express atomic and molecular distances.

    Input: bohr_radius: Value in bohr radius units
    
    Returns: Value in angstrom units
    """
    angstrom = bohr_radius * 0.52917721067
    return angstrom


# Creating spatial range generator as a function for repeated use throughout program
def generate_x(x_min, x_max, N):
    delta_x = (x_max - x_min)/N
    x = np.arange(x_min, x_max + delta_x, delta_x) #arguments(min,max,step_size) max is given as x_max + delta_x as it is non inclusive of maximum, adding one more increment of delta_x fixes this and auto scales with user choice of N
    return(x, delta_x)