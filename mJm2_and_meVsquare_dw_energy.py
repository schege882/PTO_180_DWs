"""
A code to compute energy of Domain Wall(DW) in mJ/m^2
This code calculates the DW energy of a 20 x 1 x 1 PbTiO3
supercell.
8th May 2025 at 10:20
By Stephen Chege
"""
# Getting the energy of the supercell in eV
# ----------------------
# Fully relaxed
# energy_supercell = -173374.208988   # Ising
#energy_supercell = -173374.219176   # Ising + Neel
#energy_supercell = -173374.225949   # Ising + Neel + Bloch
energy_supercell = -173381.833949   # Ising + Neel + Bloch --> From Louis (0.0025 eV/A)

# Get the lattice parameter b in Ang
#lattice_b = 3.889483                # Ising
#lattice_b = 3.888776                # Ising + Neel
#lattice_b = 3.892561                # Ising + Neel + Bloch
#lattice_b = 3.897                # Ising + Neel + Bloch --> From PRX
lattice_b = 3.8843                # Ising + Neel + Bloch --> From Louis

# Get the lattice parameter c in Ang
#lattice_c = 4.116203               # Ising
#lattice_c = 4.116656               # Ising + Neel
#lattice_c = 4.114941               # Ising + Neel + Bloch
# lattice_c = 4.075               # Ising + Neel + Bloch --> From PRX
lattice_c = 4.122                # Ising + Neel + Bloch --> From Louis
# ----------------------

# ----------------------
# a = b = 3.889 Ang, fixed SrTiO3
#energy_supercell = -173374.208637   # Ising
#energy_supercell = -173374.218806   # Ising + Neel
#energy_supercell = -173374.224547   # Ising + Neel + Bloch

# Get the lattice parameter b in Ang
#lattice_b = 3.889                   # Ising
#lattice_b = 3.889                   # Ising + Neel
#lattice_b = 3.889                   # Ising + Neel + Bloch

# Get the lattice parameter c in Ang
#lattice_c = 4.120255                # Ising
#lattice_c = 4.119537                # Ising + Neel
#lattice_c = 4.120357                # Ising + Neel + Bloch
# ----------------------

# ----------------------
# a = b = 3.912274 Ang, fixed cubic DyScO3
#energy_supercell = -173374.152920   # Ising
#energy_supercell = -173374.162818   # Ising + Neel
#energy_supercell = -173374.182787   # Ising + Neel + Bloch

# Get the lattice parameter b in Ang
#lattice_b = 3.912274                   # Ising
#lattice_b = 3.912274                # Ising + Neel
#lattice_b = 3.912274                # Ising + Neel + Bloch

# Get the lattice parameter c in Ang
#lattice_c = 4.068481                # Ising
#lattice_c = 4.068318                # Ising + Neel
#lattice_c = 4.071091                # Ising + Neel + Bloch
# ----------------------

# ----------------------
# a = 3.912274 Ang, b = 3.915790 fixed orthorrhombic DyScO3
#energy_supercell = -173374.142024   # Ising
#energy_supercell = -173374.153145   # Ising + Neel
#energy_supercell = -173374.174325   # Ising + Neel + Bloch

# Get the lattice parameter b in Ang
#lattice_b = 3.915790                   # Ising
#lattice_b = 3.915790                # Ising + Neel
#lattice_b = 3.915790                # Ising + Neel + Bloch

# Get the lattice parameter c in Ang
#lattice_c = 4.065017                # Ising
#lattice_c = 4.066235                # Ising + Neel
#lattice_c = 4.068537                # Ising + Neel + Bloch
# ----------------------

# ----------------------
# b = 3.912274 Ang, a = 3.915790 fixed orthorrhombic DyScO3
#energy_supercell =  -173374.144250  # Ising
#energy_supercell = -173374.154174   # Ising + Neel
#energy_supercell = -173374.173931   # Ising + Neel + Bloch

# Get the lattice parameter b in Ang
#lattice_b = 3.912274                   # Ising
#lattice_b = 3.912274                # Ising + Neel
#lattice_b = 3.912274                # Ising + Neel + Bloch

# Get the lattice parameter c in Ang
#lattice_c = 4.067192                # Ising
#lattice_c = 4.067334                # Ising + Neel
#lattice_c = 4.064939                # Ising + Neel + Bloch
# ----------------------
# ----------------------
# Fixed to optimized bulk tetragonal ferroelectric cell
#energy_supercell = -173374.144900   # Ising
#energy_supercell = -173374.158046   # Ising + Neel
#energy_supercell = -173374.162473   # Ising + Neel + Bloch

# Get the lattice parameter b in Ang
#lattice_b = 3.870565                   # Ising
#lattice_b = 3.870565                # Ising + Neel
#lattice_b = 3.870565                # Ising + Neel + Bloch

# Get the lattice parameter c in Ang
#lattice_c = 4.220001                # Ising
#lattice_c = 4.220001                # Ising + Neel
#lattice_c = 4.220001                # Ising + Neel + Bloch
# ----------------------

def dw_energy(energy_supercell, lattice_b, lattice_c):
    #Number of unit cells in the supercell (In our case 20 x 1 x 1)
    number_uc = 20

    # Energy of relaxed bulk tetragonal ferroelectric unit cell in eV
    energy_tetra = -8668.729994
    energy_tetra = -93909.02545 # Abinit

    # Energy of DW in eV per unit cell
    dw_energy_in_eV_uc = (float(energy_supercell)-number_uc * energy_tetra)*0.5    
    # print(dw_energy_in_eV_uc, " eV per unit cell")

    # Convert DW energy from eV to mJ
    eV2J = 1.6022e-19
    dw_energy_in_mJ_uc = dw_energy_in_eV_uc * eV2J * 1.e3
    # print(dw_energy_in_mJ_uc, "mJ")
    
    # Area of PbO plane lattice_b x lattice_c, b and c are in Ang
    area_in_meters_squared = float(lattice_b) * float(lattice_c) * 1.e-20
    # print(area_in_meters_squared, "m^2")

    # Energy of DW in eV per unit cell area
    energy_in_mJ_per_meter_squared = (dw_energy_in_mJ_uc / area_in_meters_squared)
    print(energy_in_mJ_per_meter_squared, "mJ/m^2")

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # From mJ/m^2 to meV/$\square$  %
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    mJ2meV = 1 / eV2J
    
    # From mJ/m^2 to meV/m^2
    energy_in_meV_per_meter_squared = energy_in_mJ_per_meter_squared * mJ2meV

    # From meV/m^2 to meV/$square$ 
    # where $\square$ represents the cell surface area of the DW
    energy_in_meV_per_square = energy_in_meV_per_meter_squared * area_in_meters_squared

    print(energy_in_meV_per_square, "meV/$square$")


dw_energy(energy_supercell, lattice_b, lattice_c)
