#!/usr/bin/python3
# Plot multiple 1D curves from postprocessing output (2D)
# Give files as input arguments

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pathlib import Path
import sys

######################## SET PARAMETERS HERE ###################################
fs = 16 # fontsize
gamma_val = 0.0 # Gamma to plot (exact value, used to pick data lines)
################################################################################

fig = plt.figure(figsize=(10,8))
ax = plt.subplot(111)

infiles = sys.argv[1:]

for infile in infiles:

    a = np.loadtxt(infile)

    # Filter only wanted gamma values
    a = a[a[:,1]==gamma_val]
    r = a[:,0]
    gamma = a[:,1]
    E = a[:,2]

    p1 = ax.plot(r, E, linewidth=3, label=str(infile[-19:-4]))
    ax.set_xlabel(r'$r$ ($\mathrm{\AA}$)', fontsize=fs)
    ax.set_ylabel(r'$E$ (eV)', fontsize=fs)
    ax.set_xlim([7, 15])
    ax.set_ylim([-0.07, 0.04])
    ax.tick_params(labelsize=fs)

plt.grid()
plt.legend(fontsize=fs)
plt.show() 
