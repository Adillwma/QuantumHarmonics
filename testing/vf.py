import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the grid
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
z = np.linspace(-5, 5, 100)
X, Y, Z = np.meshgrid(x, y, z)

# Define constants
l = 2

# Define the function for the electric potential of a hydrogen atom
def hydrogen_potential(x, y, z, l):
    r = np.sqrt(x**2 + y**2 + z**2)
    V_hyd = -2/r + (l*(l+1)/r**2)    
    return V_hyd

"""

## 3D Vector Field Plot
# Calculate the gradient of the electric potential
dx, dy, dz = np.gradient(hydrogen_potential(X, Y, Z, l), x, y, z)

# Plot
fig = plt.figure(figsize=(20, 20))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, dx, dy, dz, length=0.5, normalize=True, alpha=0.3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Electric Field Due to Hydrogen Atom')
plt.show()
"""


# imshow plot the flat projections of the vector field onto each axis


# Calculate the gradient of the electric potential
dx, dy, dz = np.gradient(hydrogen_potential(X, Y, Z, l), x, y, z)

# imshow plot the flat projections of the vector field onto each axis
fig, ax = plt.subplots(1, 3, figsize=(60, 20))
ax[0].imshow(dx[10, :, :], cmap='RdGy', extent=[-5, 5, -5, 5])
ax[0].set_xlabel('Y')
ax[0].set_ylabel('Z')
ax[0].set_title('dV/dx')
ax[1].imshow(dy[:, 10, :], cmap='RdGy', extent=[-5, 5, -5, 5])
ax[1].set_xlabel('X')
ax[1].set_ylabel('Z')
ax[1].set_title('dV/dy')
ax[2].imshow(dz[:, :, 10], cmap='RdGy', extent=[-5, 5, -5, 5])
ax[2].set_xlabel('X')
ax[2].set_ylabel('Y')
ax[2].set_title('dV/dz')
plt.show()











# show sam eplot but slice the data in half so we can see the vectors in the centree better
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the grid
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
z = np.linspace(-5, 5, 20)
X, Y, Z = np.meshgrid(x, y, z)



# Define the function for the electric potential of a hydrogen atom
def hydrogen_potential(x, y, z, l):
    r = np.sqrt(x**2 + y**2 + z**2)
    V_hyd = -2/r + (l*(l+1)/r**2)    
    return V_hyd

# Calculate the gradient of the electric potential
dx, dy, dz = np.gradient(hydrogen_potential(X, Y, Z, l), x, y, z)

# Plot
fig = plt.figure(figsize=(20, 20))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X[:10, :, :], Y[:10, :, :], Z[:10, :, :], dx[:10, :, :], dy[:10, :, :], dz[:10, :, :], length=0.5, normalize=True, alpha=0.3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Electric Field Due to Hydrogen Atom')
plt.show()



# show potential in 2d
import numpy as np
import matplotlib.pyplot as plt

# Define the grid

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

# Define constants
# Define the function for the electric potential of a hydrogen atom

def hydrogen_potential(x, y, l):

    r = np.sqrt(x**2 + y**2)

    V_hyd = -2/r + (l*(l+1)/r**2)    

    return V_hyd


# Calculate the electric potential

V = hydrogen_potential(X, Y, l)

# Plot

plt.figure(figsize=(10, 10))

plt.contourf(X, Y, V, 100, cmap='RdGy')

plt.colorbar(label='Electric Potential (V)')

plt.xlabel('X')

plt.ylabel('Y')

plt.title('Electric Potential Due to Hydrogen Atom')

plt.show()


