#################################################
# A code for plotting layer by layer            #
# polarization of PbTiO3, 20 x 1 x 1 supercell. #
# By Stephen Chege                              #
# Date 28th March 2025, 14:26                   #
#################################################

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

## -------------------------------------------- LOAD DATA ------------------------------------- ##

# Load the data, skipping the header
polarization_data = np.loadtxt("PbTiO3.XV.P.dat", comments="#")

# ABINIT polarization data
abinit_pol_data = np.loadtxt("results_pol_fullyrelaxed.dat", comments="#")

# Extract columns for SIESTA polarization data
x_supercell = polarization_data[:, 0] #Length of supercell along x-axis in Angstroms
Pz = polarization_data[:, 3] # Ising polarization values
Px = polarization_data[:, 1] # Ising + Neel polarization values
Py = polarization_data[:, 2] # Ising + Neel + Bloch

# Extract columns for ABINIT data
# abinit_cell_number = abinit_pol_data[:,0] # unit cell number
abinit_layer_pos = abinit_pol_data[:,0] # layer position in Ang
abinit_Pz = abinit_pol_data[:,3] # Ising polarization values
abinit_Px = abinit_pol_data[:,1] # Ising + Neel polarization values
abinit_Py = abinit_pol_data[:,2] # Ising + Neel + Bloch


# Create alternating labels for PbO and TiO2 layers (SIESTA)
X_label = []

for i in range(len(x_supercell)):
    if i % 2 == 0:
        X_label.append("PbO")
    else:
        X_label.append("TiO$_2$")

    
## -------------------------------------------- PLOT DATA ------------------------------------- ##
# Plotting
plt.rcParams["font.family"] = "Times New Roman" # Apply Times New Roman font

# # Create a figure with specific size
fig, ax = plt.subplots(1, 1, figsize=(8, 6), constrained_layout=True) # row, column, image size


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#       SIESTA & ABINIT PLOT          %
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ----- SIESTA PLOT --------#
ax.plot(x_supercell, Pz, linestyle='solid', color='red') # plot Ising polarization profile
ax.plot(x_supercell, Px, linestyle='solid', color='green') # plot Ising + Neel polarization profile
ax.plot(x_supercell, Py, linestyle='solid', color='blue') # plot Ising + Neel + Bloch polarization profile

# ----- ABINIT PLOT --------#
ax.plot(abinit_layer_pos, abinit_Pz, linestyle='dashed', color='red') # plot Ising polarization profile
ax.plot(abinit_layer_pos, abinit_Px, linestyle='dashed', color='green') # plot Ising + Neel polarization profile
ax.plot(abinit_layer_pos, abinit_Py, linestyle='dashed', color='blue') # plot Ising + Neel + Bloch polarization profile


# Set axis labels
ax.set_ylabel("P$_z$", fontsize=16)

# Alternating PbO and TiO2 labels on the x-axis
ax.set_xticks(x_supercell) # sets tick labels at the position(in Angstroms) of the PbO
                           # or TiO2 layer.
ax.set_xticklabels(X_label, rotation=90) 

# Change label size on ticks
ax.tick_params(axis='both', labelsize=14)

# set length of axis
ax.set_xlim([x_supercell[0]-1, x_supercell[-1]+1])
ax.set_ylim([np.min(Pz)-0.1, np.max(Pz)+0.1])

# Draw vertical line at PbO centre DW plane
x_vert = x_supercell[int(len(x_supercell)/2)] # line position in x-axis
ax.axvline(x=x_vert, color='black', linestyle='-.')

# Place (a) label on the plot
ax.text(x_supercell[0], np.max(Pz), "(a)", fontsize=14)

# *******************************************
# **** Inset Plot for the Neel component ****
# ******************************************* 
# Inset focus of x-axis around DW 
WINDOW = 6 # number of layers away from center of DW
CODW = int(len(x_supercell) / 2) # center of DW
x_axis_inset_coord_siesta = x_supercell[CODW - WINDOW: CODW + WINDOW]
x_axis_inset_coord_abinit = abinit_layer_pos[CODW - WINDOW: CODW + WINDOW]

# Px polarization values around DW
y_axis_inset_coord_siesta = Px[CODW - WINDOW:CODW+WINDOW]
y_axis_inset_coord_abinit = abinit_Px[CODW - WINDOW:CODW+WINDOW]


# Inset plot
inset_ax = inset_axes(ax, width="38%", height="30%", loc="upper right", borderpad=0.5)
inset_ax.plot(x_axis_inset_coord_siesta, y_axis_inset_coord_siesta, linestyle='solid', color='green') # siesta
inset_ax.plot(x_axis_inset_coord_abinit, y_axis_inset_coord_abinit, linestyle='dashed', color='green') # abinit


# set tick label size
inset_ax.tick_params(axis='both', labelsize=12)

# Alternating PbO and TiO2 labels on the x-axis, for the inset plot
inset_ax.set_xticks(x_axis_inset_coord_siesta) # sets tick labels at the position(in Angstroms) of the PbO
                           # or TiO2 layer.
inset_ax.set_xticklabels(X_label[CODW - WINDOW:CODW+WINDOW], rotation=90) 

# # remove xticks
# inset_ax.set_xticks([])

# set length of axis
inset_ax.set_xlim([x_supercell[CODW - WINDOW]-1, x_supercell[CODW + WINDOW]])
inset_ax.set_ylim([np.min(Px)-0.0015, np.max(Px)+0.0015])

# Draw vertical line at PbO centre DW plane
inset_ax.axvline(x=x_vert, color='black', linestyle='-.')

# save figure
plt.savefig("abinit-siesta-fully-relaxed-supercell-pol_profile.png", dpi=300)

# Show plot
plt.show()
