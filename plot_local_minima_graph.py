#!/usr/bin/python3
# Plot line graph of the local minima results (2D)
# Give local-minima data file as argument

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pathlib import Path
import sys

fig = plt.figure(figsize=(8,6))
ax = plt.subplot(111)

r, gamma, E, nu = np.loadtxt(sys.argv[1], unpack='TRUE')
N = np.size(r)
xval = np.arange(N)+1

p1 = ax.plot(xval, E, 'b-', linewidth=3)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.set_xlabel('Local minimum no.')
ax.set_ylabel(r'$E_\mathrm{ads}$ (eV)')
plt.grid()
plt.tight_layout()
plt.show() 
