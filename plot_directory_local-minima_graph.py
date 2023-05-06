#!/usr/bin/python3
# Plot line graph of the local minima results
# for all local-minima files in the folder
# Give folder path as input argument

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pathlib import Path
import sys

fig = plt.figure(figsize=(20,20))
ax = plt.subplot(111)

# Get number of files to specify colors
Nfiles = 0
for infile in Path().glob(str(sys.argv[1]) + 'it*npts*.dat'):
    Nfiles = Nfiles + 1
cols = np.linspace(0.8, 0, Nfiles)


for ind, infile in enumerate(Path().glob(str(sys.argv[1]) + 'it*npts*.dat')):

    r, gamma, E, nu = np.loadtxt(infile, unpack=True)
    N = np.size(r)
    xval = np.arange(N)+1

    if ind < Nfiles - 1:
        p1 = ax.plot(xval, r, linewidth=3, \
                c=(cols[ind], cols[ind], cols[ind]), \
                label=str(infile)[-19:-13])
    else:
        p1 = ax.plot(xval, E, linewidth=3, c='r', label=str(infile)[-19:-13])
    ax.yaxis.grid(True, which='major', color='k')
    ax.yaxis.grid(True, which='minor', linestyle=':')
    ax.xaxis.grid(True, which='major', color='k')
    ax.xaxis.grid(True, which='minor', linestyle=':')

plt.legend()
plt.show() 
