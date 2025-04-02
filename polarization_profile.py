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

# Create alternating labels for PbO and TiO2 layers (ABINIT)
abinit_X_label = []

for i in range(len(abinit_layer_pos)):
    if i % 2 == 0:
        abinit_X_label.append("PbO")
    else:
        abinit_X_label.append("TiO$_2$")

# Create label and its tick position for each unit cell (ABINIT)
# abinit_X_label = []
# abinit_xtick_position = []

# for value in abinit_cell_number:
#     abinit_X_label.append("PTO")
#     xtick_pos = value + 0.5
#     abinit_xtick_position.append(xtick_pos)
    
## -------------------------------------------- PLOT DATA ------------------------------------- ##
# Plotting
plt.rcParams["font.family"] = "Times New Roman" # Apply Times New Roman font

# Create a figure with specific size
fig, ax = plt.subplots(2, 1, figsize=(8, 7), constrained_layout=True) # row, column, image size

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#       ABINIT PLOT         %
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%
ax[0].plot(abinit_layer_pos, abinit_Pz, color='red')  # plot Ising polarization profile
ax[0].plot(abinit_layer_pos, abinit_Px, color='green')  # plot Ising polarization profile
ax[0].plot(abinit_layer_pos, abinit_Py, color='blue')  # plot Ising polarization profile

# y-axis label
ax[0].set_ylabel("Polarization in C/m$^2$", fontsize=12)

# Set x-axis ticks and tick labels
ax[0].set_xticks(abinit_layer_pos) # ticks
ax[0].set_xticklabels(abinit_X_label, rotation=90) # tick labels

# set length of axis
ax[0].set_xlim([abinit_layer_pos[0]-1, abinit_layer_pos[-1]+1])
ax[0].set_ylim([np.min(abinit_Pz)-0.1, np.max(abinit_Pz)+0.1])

# *******************************************
# **** Inset Plot for the Neel component ****
# ******************************************* 
abinit_inset_ax = inset_axes(ax[0], width="40%", height="30%", loc="upper right", borderpad=1)
abinit_inset_ax.plot(abinit_layer_pos, abinit_Px, color='green')

# set tick label size
abinit_inset_ax.tick_params(labelsize=7)

# set length of axis
abinit_inset_ax.set_xlim([abinit_layer_pos[0]-1, abinit_layer_pos[-1]+1])
abinit_inset_ax.set_ylim([np.min(abinit_Px)-0.0005, np.max(abinit_Px)+0.0005])

# remove xticks
abinit_inset_ax.set_xticks([])



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#       SIESTA PLOT          %
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
ax[1].plot(x_supercell, Pz, color='red') # plot Ising polarization profile
ax[1].plot(x_supercell, Px, color='green') # plot Ising + Neel polarization profile
ax[1].plot(x_supercell, Py, color='blue') # plot Ising + Neel + Bloch polarization profile

# Set axis labels
ax[1].set_ylabel("Polarization (C/m$^2$)", fontsize=12)

# Alternating PbO and TiO2 labels on the x-axis
ax[1].set_xticks(x_supercell) # sets tick labels at the position(in Angstroms) of the PbO
                           # or TiO2 layer.
ax[1].set_xticklabels(X_label, rotation=90) 

# set length of axis
ax[1].set_xlim([x_supercell[0]-1, x_supercell[-1]+1])
ax[1].set_ylim([np.min(Pz)-0.1, np.max(Pz)+0.1])

# *******************************************
# **** Inset Plot for the Neel component ****
# ******************************************* 
inset_ax = inset_axes(ax[1], width="40%", height="30%", loc="upper right", borderpad=1)
inset_ax.plot(x_supercell, Px, color='green')

# set tick label size
inset_ax.tick_params(labelsize=7)

# Alternating PbO and TiO2 labels on the x-axis, for the inset plot
# inset_ax.set_xticks(x_supercell) # sets tick labels at the position(in Angstroms) of the PbO
#                            # or TiO2 layer.
# inset_ax.set_xticklabels(X_label, rotation=90) 

# set length of axis
inset_ax.set_xlim([x_supercell[0]-1, x_supercell[-1]+1])
inset_ax.set_ylim([np.min(Px)-0.0005, np.max(Px)+0.0005])

# remove xticks
inset_ax.set_xticks([])

# save figure
plt.savefig("abinit-siesta-pol_profile.png", dpi=300)

# Show plot
plt.show()


