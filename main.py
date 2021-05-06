import matplotlib.pyplot as plt
import numpy as np
from skyrmions import *
from scipy.stats.kde import gaussian_kde

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

# compute the magnetic moments
spinx, spiny = antiskyrmion(X, Y, n=2, r=1)
# compute the deflection of the moments
xim, yim = deflect(X, Y, spinx, spiny, scale=0.1)
xim = xim.flatten()
yim = yim.flatten()

# taken from https://stackoverflow.com/a/36958298/5934316
k = gaussian_kde(np.vstack([xim, yim]))
xi, yi = np.mgrid[xim.min():xim.max():xim.size**0.5*1j,
                  yim.min():yim.max():yim.size**0.5*1j]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))

vmin = 0.073
vmax = 0.077
d = 1.25
ax1.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='auto', 
               cmap="gray", vmin=vmin, vmax=vmax)
ax1.set_xlim((-d, d))
ax1.set_ylim((-d, d))

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

d = 1.5
ax2.set_xlim((-d, d))
ax2.set_ylim((-d, d))

# Format axes to not show ticks and labels and remove spaces
for ax in [ax1, ax2]:
    ax.axis("off")

plt.subplots_adjust(top=1.0,
                    bottom=0.0,
                    left=0.0,
                    right=1.0,
                    hspace=0,
                    wspace=0)

plt.show()
