# LTEM-contrast
Script to calculate the contrast that certain 2D spin structures would produce under a Lorentz transmission electron microscope (LTEM).

Electrons are modeled to impinge on the spin structure on a discrete 2D grid at an angle of 90°. In the in-plane B-field of the structure, which is equal to its magnetization due to magnetic shape anisotropy, electrons are deflected by the Lorentz force into a direction perpendicular to their velocity and the local spin direction of the spin structure. The impact points of these deflected electrons on the virtual detector is stored in a histogram and is converted to a continuous probability density using the kdeplot function from the seaborn Python library.

Analytical functions to create spin structures are found in skyrmions.py, while the main code is found in main.py.
