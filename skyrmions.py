# Functions defining various 2D chiral and non-chiral spin structures
# Parameters:   r - Radius
#               n - Order of polynomial increase around zero
#                   and order of the antiskyrmion
#               w - Winding number for Bloch and Néel Skysmions
#
# Returns spin direction (xs, ys) at input point (x, y)
# (d, phi) are transformations of (x, y) to polar coordinates

import numpy as np

def neelskysmion(x, y, r=1, n=1, w=1):
    d = np.sqrt(x*x + y*y)
    xs = w*x/d
    ys = w*y/d
    xs *= d**n*np.exp(-3*(d/r)**2)
    ys *= d**n*np.exp(-3*(d/r)**2)
    return xs, ys

def blochskysmion(x, y, r=1, n=1, w=1):
    d = np.sqrt(x*x + y*y)
    phi = np.arctan2(y, x)
    xs = -w*d**n*np.exp(-3*(d/r)**2)*np.sin(phi)
    ys = w*d**n*np.exp(-3*(d/r)**2)*np.cos(phi)
    return xs, ys

def antiskyrmion(x, y, r=1, n=1):
    d = np.sqrt(x*x + y*y)
    phi = np.arctan2(y, x) + np.pi/2
    xs = d**n*np.exp(-3*(d/r)**2)*np.sin(n*phi - np.pi/2)
    ys = d**n*np.exp(-3*(d/r)**2)*np.cos(n*phi - np.pi/2)
    return xs, ys

def bubble(x, y, r=1, n=1):
    d = np.sqrt(x*x + y*y)
    phi = np.arctan2(y, x)
    xs = -1/np.sqrt(2)*np.sin(2*phi)
    ys = np.sqrt(1 - xs*xs)
    xs *= d**n*np.exp(-3*(d/r)**2)
    ys *= d**n*np.exp(-3*(d/r)**2)
    return xs, ys

def neelbubble(x, y, r=1, n=1):
    d = np.sqrt(x*x + y*y)
    phi = np.arctan2(y, x)
    ys = -1/np.sqrt(2)*np.sin(2*phi)
    xs = -np.sqrt(1 - ys*ys)
    xs *= d**n*np.exp(-3*(d/r)**2)
    ys *= d**n*np.exp(-3*(d/r)**2)
    return xs, ys