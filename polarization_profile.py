#################################################
# A code for plotting layer by layer            #
# polarization of PbTiO3, 20 x 1 x 1 supercell. #
# By Stephen Chege                              #
# Date 28th March 2025, 14:26                   #
#################################################

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Load the data, skipping the header
polarization_data = np.loadtxt("PbTiO3.XV.P.dat", comments="#")

# Extract columns
x_supercell = polarization_data[:, 0] #Length of supercell along x-axis in Angstroms
Pz = polarization_data[:, 3] # Ising polarization values
Px = polarization_data[:, 1] # Ising + Neel polarization values
Py = polarization_data[:, 2] # Ising + Neel + Bloch


# Create alternating labels for PbO and TiO2 layers
X_label = []

for i in range(len(x_supercell)):
    if i % 2 == 0:
        X_label.append("PbO")
    else:
        X_label.append("TiO$_2$")


# Plotting
plt.rcParams["font.family"] = "Times New Roman" # Apply Times New Roman font
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_supercell, Pz, color='red') # plot Ising polarization profile
ax.plot(x_supercell, Px, color='green') # plot Ising + Neel polarization profile
ax.plot(x_supercell, Py, color='blue') # plot Ising + Neel + Bloch polarization profile

# Set axis labels
# ax.set_xlabel(" ")
ax.set_ylabel("Polarization (C/m$^2$)", fontsize=12)

# Alternating PbO and TiO2 labels on the x-axis
ax.set_xticks(x_supercell) # sets tick labels at the position(in Angstroms) of the PbO
                           # or TiO2 layer.
ax.set_xticklabels(X_label, rotation=90) 

# set length of axis
ax.set_xlim([x_supercell[0]-1, x_supercell[-1]+1])
ax.set_ylim([np.min(Pz)-0.1, np.max(Pz)+0.1])

# *******************************************
# **** Inset Plot for the Neel component ****
# ******************************************* 
inset_ax = inset_axes(ax, width="40%", height="30%", loc="upper right", borderpad=1)
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
plt.savefig("polarization_profile.png", dpi=300)

# Show plot
plt.show()


