#!/usr/bin/python3
# Batch plot 2D landscapes from BOSS postprocessing data
# Give input postprocessing directory as an argument
# Output is plotted into postprocessing directories "fig_*"

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from pathlib import Path

############# SET PARAMETERS HERE ##############
Nx = 50 # Number of data points
Ny = 50
xlabel = r'$r$ $\mathrm{(\AA)}$' # Axis labels
ylabel = r'$\gamma$ (deg)'
fs_tick = 14 # Plot font sizes
fs_label = 14
acq_ms = 3 # Acquisition marker size
acq_c = 'r' # Acquisition marker color
pred_ms = 6 # Predicted minimum marker size
pred_c = 'w' # Predicted minimum marker color
next_ms = 6 # Next point marker size
next_c = 'm' # Next point marker color
plot_points = True # Switch to plot acq points
plot_minimum = True # Switch to plot predicted minimum
plot_next = True # Switch to plot next acquisition point
################################################

indir = sys.argv[1] + '/' # Add slash, just in case
indir_mod = indir + 'data_models/'
indir_acq = indir + 'data_acqfns/'
outdir_mod = indir + 'fig_models/'
outdir_var = indir + 'fig_uncert/'
outdir_acq = indir + 'fig_acqfns/'

# Create output directories if do not exist
Path(outdir_mod).mkdir(parents=True, exist_ok=True)
Path(outdir_var).mkdir(parents=True, exist_ok=True)
Path(outdir_acq).mkdir(parents=True, exist_ok=True)

# Determine file names
fnames = [f for f in os.listdir(indir_mod) if \
        os.path.isfile(os.path.join(indir_mod, f))]
iters = np.array([], dtype='int') # Iteration numbers
pts = np.array([], dtype='int') # Number of points
for f in fnames:
    iters = np.append(iters, int(f[2:6]))
    pts = np.append(pts, int(f[11:15]))
iters = np.sort(iters)
pts = np.sort(pts)

# Load acquisition points
acqpt_iter, acqpt_npts, acqpt_x1, acqpt_x2, acqpt_val = np.loadtxt(indir + 'acquisitions.dat', unpack=True)

# Load minimum predictions
pred_iter, pred_npts, pred_x1, pred_x2, pred_val, pred_var = np.loadtxt(indir + \
        'minimum_predictions.dat', unpack=True)

# Plot all files
for i in np.arange(np.size(iters)):
    in_fname = 'it' + str(iters[i]).zfill(4) + '_npts' \
            + str(pts[i]).zfill(4) + '.dat'
    mod_x1, mod_x2, mod_ene, mod_var = np.loadtxt(indir_mod + in_fname, unpack=True)
    acq_x1, acq_x2, acq_val = np.loadtxt(indir_acq + in_fname, unpack=True)

    # Shape data to square arrays
    mod_x1 = mod_x1.reshape(Nx, Ny)
    mod_x2 = mod_x2.reshape(Nx, Ny)
    mod_ene = mod_ene.reshape(Nx, Ny)
    mod_var = mod_var.reshape(Nx, Ny)
    acq_x1 = acq_x1.reshape(Nx, Ny)
    acq_x2 = acq_x2.reshape(Nx, Ny)
    acq_val = acq_val.reshape(Nx, Ny)

    # Plot models
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    p1 = ax.contourf(mod_x1, mod_x2, mod_ene, 30, cmap='viridis')
    p2 = ax.contour(mod_x1, mod_x2, mod_ene, 30, colors='k', linewidths=(0.2,))
    if plot_points: # Plot acquisition points
        p3 = ax.plot(acqpt_x1[:pts[i]], acqpt_x2[:pts[i]], c=acq_c, ls="None",
                marker='o', ms=acq_ms)
    if plot_minimum: # Plot predicted minimum
        p4 = ax.plot(pred_x1[iters[i]], pred_x2[iters[i]], c=pred_c, ls="None",
                marker='x', markeredgewidth=2, ms=pred_ms)
    if plot_next and pts[i] != pts[-1]: # Plot next acquisition point 
        p5 = ax.plot(acqpt_x1[pts[i]], acqpt_x2[pts[i]], c=next_c, ls="None",
                marker='^', ms=next_ms)
    plt.rcParams.update({'font.size': fs_tick})
    ax.set_xlabel(xlabel, fontsize=fs_label)
    ax.set_ylabel(ylabel, fontsize=fs_label)
    ax.tick_params(labelsize=fs_tick)
    cb = fig.colorbar(p1, shrink=0.5, aspect=6, pad = 0.05)
    cb.ax.tick_params(labelsize=fs_tick)
    plt.tight_layout()
    out_fname = 'it' + str(iters[i]).zfill(4) + '_npts' \
            + str(pts[i]).zfill(4) + '.png'
    plt.savefig(outdir_mod + out_fname, format='png', dpi=200, bbox_inches='tight')
    plt.close()

    # Plot uncertainty
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    p1 = ax.contourf(mod_x1, mod_x2, mod_var, 30, cmap='viridis')
    p2 = ax.contour(mod_x1, mod_x2, mod_var, 30, colors='k', linewidths=(0.2,))
    if plot_points: # Plot acquisition points
        p3 = ax.plot(acqpt_x1[:pts[i]], acqpt_x2[:pts[i]], c=acq_c, ls="None",
                marker='o', ms=acq_ms)
    if plot_minimum: # Plot predicted minimum
        p4 = ax.plot(pred_x1[iters[i]], pred_x2[iters[i]], c=pred_c, ls="None",
                marker='x', markeredgewidth=2, ms=pred_ms)
    if plot_next and pts[i] != pts[-1]: # Plot next acquisition point 
        p5 = ax.plot(acqpt_x1[pts[i]], acqpt_x2[pts[i]], c=next_c, ls="None",
                marker='^', ms=next_ms)
    plt.rcParams.update({'font.size': fs_tick})
    ax.set_xlabel(xlabel, fontsize=fs_label)
    ax.set_ylabel(ylabel, fontsize=fs_label)
    ax.tick_params(labelsize=fs_tick)
    cb = fig.colorbar(p1, shrink=0.5, aspect=6, pad = 0.05)
    cb.ax.tick_params(labelsize=fs_tick)
    plt.tight_layout()
    out_fname = 'it' + str(iters[i]).zfill(4) + '_npts' \
            + str(pts[i]).zfill(4) + '_uncert.png'
    plt.savefig(outdir_var + out_fname, format='png', dpi=200, bbox_inches='tight')
    plt.close()

    # Plot next acquisition
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    p1 = ax.contourf(acq_x1, acq_x2, acq_val, 30, cmap='viridis')
    p2 = ax.contour(acq_x1, acq_x2, acq_val, 30, colors='k', linewidths=(0.2,))
    if plot_points: # Plot acquisition points
        p3 = ax.plot(acqpt_x1[:pts[i]], acqpt_x2[:pts[i]], c=acq_c, ls="None",
                marker='o', ms=acq_ms)
    if plot_minimum: # Plot predicted minimum
        p4 = ax.plot(pred_x1[iters[i]], pred_x2[iters[i]], c=pred_c, ls="None",
                marker='x', markeredgewidth=2, ms=pred_ms)
    if plot_next and pts[i] != pts[-1]: # Plot next acquisition point 
        p5 = ax.plot(acqpt_x1[pts[i]], acqpt_x2[pts[i]], c=next_c, ls="None",
                marker='^', ms=next_ms)
    plt.rcParams.update({'font.size': fs_tick})
    ax.set_xlabel(xlabel, fontsize=fs_label)
    ax.set_ylabel(ylabel, fontsize=fs_label)
    ax.tick_params(labelsize=fs_tick)
    cb = fig.colorbar(p1, shrink=0.5, aspect=6, pad = 0.05)
    cb.ax.tick_params(labelsize=fs_tick)
    plt.tight_layout()
    out_fname = 'it' + str(iters[i]).zfill(4) + '_npts' \
            + str(pts[i]).zfill(4) + '.png'
    plt.savefig(outdir_acq + out_fname, format='png', dpi=200, bbox_inches='tight')
    plt.close()
