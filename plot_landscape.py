#!/usr/bin/python3
# Plot 2D landscape from BOSS postprocessing data

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

############# SET PARAMETERS HERE ##############
Nx = 50 # Number of data points
Ny = 50
fs_tick = 14 # Plot font sizes
fs_label = 14
range_min = -0.07 # Plot ranges
range_max = 0
################################################

infile = sys.argv[1]

### For model and uncert
x1, x2, ene, var = np.loadtxt(infile, unpack=True) # Model/uncert
x1 = x1.reshape(Nx, Ny)
x2 = x2.reshape(Nx, Ny)
ene = ene.reshape(Nx, Ny)
var = var.reshape(Nx, Ny)

'''
### For acqfn
x1, x2, acq = np.loadtxt(infile, unpack=True) # Acq.fn
x1 = x1.reshape(Nx, Ny)
x2 = x2.reshape(Nx, Ny)
acq = acq.reshape(Nx, Ny)
'''

# Plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
# Replace below 'ene' with 'var' for variance plot
p1 = ax.contourf(x1, x2, ene, np.linspace(range_min, range_max, 30), cmap='viridis')
p2 = ax.contour(x1, x2, ene, np.linspace(range_min, range_max, 30), colors='k', linewidths=(0.3,))
plt.rcParams.update({'font.size': fs_tick})
ax.set_xlabel('x1', fontsize=fs_label)
ax.set_ylabel('x2', fontsize=fs_label)
ax.tick_params(labelsize=fs_tick)
cb = fig.colorbar(p1, shrink=0.5, aspect=6, pad = 0.05)
cb.ax.tick_params(labelsize=fs_tick)
plt.tight_layout()
plt.savefig('fig.png', format='png', dpi=200, bbox_inches='tight')
plt.close()
