# LTEM-contrast
Script to calculate the contrast that certain 2D spin structures would produce under a Lorentz transmission electron microscope (LTEM).

Parallel electrons are modeled to impinge on the spin structure on a discrete 2D grid at an angle of 90°. In the magnetic field of the structure, electrons are deflected by the Lorentz force into a direction perpendicular to their own velocity and the local magnetzation direction of the spin structure. The "scale" factor in the code may be adjusted to implement weaker or stronger deflection. After iterating over all electrons in the image and calculating their impact points on the virtual detector, the collected data is converted to a continuous probability density using the kdeplot function from the seaborn Python library, implementing a kernel density estimation. The result is a continuous grayscale image, where bright areas indicate areas towards which many electrons are deflected, whereas dark regions indicate regions with a below-average electron count.

The program additionally plots a representation of the spin structure as a dicrete grid of arrows, whose length and direction indicate the local orientation and magnitude of the spin structure. The arrows' colors are mapped to their direction on a HSV spectrum using the arctan2 function from the Python library numpy.

A variety of analytical functions creating 2D spin structures are found in skyrmions.py, while the main code is found in main.py, including additional comments.
