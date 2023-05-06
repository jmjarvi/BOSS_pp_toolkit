#!/usr/bin/python3
# Plot line graph of the local minima results (2D)
# for several local-minima files 
# Give files as input arguments

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pathlib import Path
import sys

fs = 16 # fontsize

fig = plt.figure(figsize=(20,20))
ax = plt.subplot(111)

infiles = sys.argv[1:]

for infile in infiles:

    r, gamma, E, nu = np.loadtxt(infile, unpack=True)
    N = np.size(r)
    xval = np.arange(N)+1

    p1 = ax.plot(xval, E, linewidth=3, label=str(infile[-19:-4]))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.yaxis.grid(True, which='major', color='k')
    ax.yaxis.grid(True, which='minor', linestyle=':')
    ax.xaxis.grid(True, which='major', color='k')
    ax.xaxis.grid(True, which='minor', linestyle=':')
    ax.set_xlabel('Iteration', fontsize=fs)
    ax.set_ylabel(r'$E$ (eV)', fontsize=fs)
    ax.tick_params(labelsize=fs)

plt.legend(fontsize=fs)
plt.show() 
