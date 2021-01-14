import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from skyrmions import *

# Function implementing the deflection of an electron crossing the spin structure 
# perpendicular to the plane by the Lorentz force. The deflection is proportional
# to the scale variable.
# Returns the final position of an electron on the camera traversing the spin
# structure with spin direction (sx, sy) at (x, y).
def deflect(x, y, sx, sy, scale=0.1):
    return x - scale*sy, y + scale*sx

# Defines system of axes to host spin structure and LTEM contrast image
# using the matplotlib library
fig, [ax1, ax2] = plt.subplots(1, 2, figsize=(14, 7))

# Initialization of meshgrid of dimension nxn
n = 100
vals = np.linspace(-1.8, 1.8, num=n)
X, Y = np.meshgrid(vals, vals)

# Initialization of arrays storing x- and y-coordinates of final electron
# positions on the detector and meshgrids for storing x- and y-components
# of the spin structure
xim, yim = [], []
spinx, spiny = np.zeros_like(X), np.zeros_like(Y)

# Iteration over all points in the image
for i, y in enumerate(vals):
    for j, x in enumerate(vals):
        # Computation of spin direction and deflected coordinates,
        # stored in temporary variables
        sx, sy = antiskyrmion(x, y, n=2, r=1)
        xim_t, yim_t = deflect(x, y, sx, sy, scale=0.1)
        
        # Append spin directions to meshgrid and final coordinates to image data
        spinx[i,j], spiny[i,j] = sx, sy
        
        xim.append(xim_t)
        yim.append(yim_t)

# Plot distribution of electrons in 2D on detector using KDE. More information:   
# https://seaborn.pydata.org/generated/seaborn.kdeplot.html
# Limit lowest and highest greyscale value by using vmin and vmax parameters.
sns.kdeplot(xim, yim, cmap='gray', n_levels=300, bw=0.05, shade=True,
            clip=((-1.6, 1.6), (-1.6, 1.6)), ax=ax1)

# Define color-array containing the directions of spins in rad
# Set min and max values to +/-pi to ensure the same color map for every structure.
skip = 4
c_array = np.arctan2(spiny[::skip, ::skip], spinx[::skip, ::skip])
c_array[0][0] = -np.pi
c_array[-1][-1] = np.pi

# Plot spin structure using plt.quiver using every 'skip'th point in the image
# The direction of arrows is color-coded to a hsv map
# Adjust size of arrows by varying scale and width parameters.
ax2.set_facecolor('k')
ax2.quiver(X[::skip, ::skip], Y[::skip, ::skip], spinx[::skip, ::skip], spiny[::skip, ::skip],
           c_array, scale=3, width=0.004, minlength=0, pivot='mid', cmap='hsv')

# Format axes to not show ticks and labels and remove spaces
for ax in [ax1, ax2]:
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    
    ax.set_xticks([])
    ax.set_yticks([])
    
    ax.set_xticklabels([])
    ax.set_yticklabels([])

plt.subplots_adjust(top=1.0,
bottom=0.0,
left=0.0,
right=1.0,
hspace=0,
wspace=0)

plt.show()