import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load the data, skipping the header
polarization_data = np.loadtxt("PbTiO3.XV.P.dat", comments="#") # Replace with your actual data

x_in_Ang = polarization_data[:,0] # Layer positions
Pz = polarization_data[:, 3] # Layer-by-layer Ising polarization values

# Get domain wall center plane
dw_center_index = int(len(x_in_Ang) / 2)
#dw_center_index = np.argmin(np.abs(Pz)) # Index of min |Pz|
dw_center_x = x_in_Ang[dw_center_index]  # Position of DW center

# Select a symmetric window around the domain wall
window = 6 # change this based on layers you want to include
dw_region_x = x_in_Ang[dw_center_index - window : dw_center_index + window] # domain wall region
dw_region_Pz = Pz[dw_center_index - window : dw_center_index + window] # Pz values


#  Define the tanh fitting function
def tanh_fit(x, Po, delta, x0):
    """
    Hyperbolic tangent function for fitting the domain wall profile.

    Parameters:
    x    : Position (Å)
    Ps   : Saturation polarization (maximum absolute Pz)
    delta: Domain wall width (Å)
    x0   : Domain wall center position (Å)

    Returns:
    Pz value at position x
    """
    return Po * np.tanh((x - x0) / delta)


# Initial parameter guesses (Po from max |Pz|, delta ~ 5 Å, x0 = dw_center_x)
initial_guess = [max(abs(dw_region_Pz)), 5.0, dw_center_x] # Po should probably use bulk tetragonal
                                                           #  polarization value

# Perform the curve fitting
params, _ = curve_fit(tanh_fit, dw_region_x, dw_region_Pz, p0=initial_guess)

# Extract the fitted domain wall width
Po_fitted, delta_fitted, x0_fitted = params

# Create alternating labels for PbO and TiO2 layers (SIESTA)
X_label = []

for i in range(len(x_in_Ang)):
    if i % 2 == 0:
        X_label.append("PbO")
    else:
        X_label.append("TiO$_2$")



# # Plotting the tanhfit
fig, ax = plt.subplots(1, 1, figsize=(8, 6), constrained_layout=True)
ax.plot(x_in_Ang, Pz, label="Ising", color="red")
ax.plot(dw_region_x, tanh_fit(dw_region_x, *params), 'c-', label="tanh fit")
ax.set_ylabel("Polarization in C/m$^2$")

# Alternating PbO and TiO2 labels on the x-axis
ax.set_xticks(x_in_Ang) # sets tick labels at the position(in Angstroms) of the PbO
                           # or TiO2 layer.
ax.set_xticklabels(X_label, rotation=90) 

# set length of axis
ax.set_xlim([x_in_Ang[0]-1, x_in_Ang[-1]+1])
ax.set_ylim([np.min(Pz)-0.1, np.max(Pz)+0.1])

#save figure
# plt.savefig("dw_width.png", dpi=300)

# plt.show()

# Print result
print(f"Estimated domain wall width: {delta_fitted:.2f} Ang")
print(f"Fitted polarization: {Po_fitted} C/m^2")
