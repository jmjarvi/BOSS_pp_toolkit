# BOSS_pp_toolkit

Scripts for visualizing Bayesian Optimization Structure Search (BOSS) postprocessing data. Further information on the BOSS method is available at https://cest-group.gitlab.io/boss/

The BOSS code can be downloaded at https://gitlab.com/cest-group/boss

Reference literature:
Todorović et al., Bayesian inference of atomistic structure in functional materials, npj Comput. Mater. 5, 35 (2019) https://doi.org/10.1038/s41524-019-0175-2
Järvi et al., Detecting stable adsorbates of (1S)-camphor on Cu(111) with Bayesian optimization, Beilstein J. Nanotechnol. 11, 1577 (2020) https://doi.org/10.3762/bjnano.11.140

## Local minima evaluation

These scripts plot the identified local minima of the model as energy plateaus to evaluate the model convergence.

plot_local_minima_graph.py: Local minima of a single iteration
plot_multiple_local-minima_graph.py: Local minima of selected iterations for comparison
plot_directory_local-minima_graph.py: Local minima of all post-processed iterartions

## Model cross-sections

These scripts help to visualize the model as 1D and 2D cross-sections.

plot_postprocessing.py: 2D landscapes of the model, uncertainty, and
acquisition function from all iterations
plot_landscape.py: A single 2D landscape
plot_multiple_1D_curves: 1D curves of selected iterations (2D data)
