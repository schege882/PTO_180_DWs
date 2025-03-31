#################################################
# A script to convert POSCAR file to XV file    #
# By Stephen Chege                              #
# 30th, March, 2025, 09:53 am EAT               #
#################################################
import numpy as np

# File name
file_name = "output_tolmxf_0.0025eVperA_HIST.poscar"    # Replace with POSCAR filename
                                                        # you wish to convert

# Read the POSCAR file
with open(file_name, 'r') as poscar_file:
    lines = poscar_file.readlines()

# Process the entire file line by line
poscar_lines = []

for line in lines:
    values = line.split()

    try:
        # Convert numeric values to float where possible and
        # keep string as it is
        processed_line = [float(val) if val.replace('.', '', 1).replace('e-', '', 1).isdigit()
                          else val for val in values] 
        # .replace('.', '', 1).replace('e-', '', 1) removes the decimal point & scientific notation
        # .isdigit() checks if the cleaned-up value is a number.

    except ValueError:
        processed_line = values

    # append values so that poscar_lines has each line from the poscar file
    poscar_lines.append(processed_line)

# Convert `poscar_lines` to a numpy array (dtype=object to handle mixed types)
poscar_numpy_array = np.array(poscar_lines, dtype=object)

# Get scaling factor from poscar_numpy_array
scaling_factor = poscar_numpy_array[1]
# print(scaling_factor) # For debugging

# Get lattice vectors from poscar_numpy_array
lattice_vectors = poscar_numpy_array[2:5]
# print(lattice_vectors) #For debugging

# Convert lattice_vectors to a numpy array of floats
lattice_vectors_numeric = np.array(lattice_vectors.tolist(), dtype=float)

# scaled_lattice_vectors
scaled_lattice_vectors = lattice_vectors_numeric * scaling_factor
# print(scaled_lattice_vectors) # For debugging

# Convert lattice vectors from Angstroms to Bohrs
lattice_vectors_in_Bohr = scaled_lattice_vectors / 0.529177 
# print(lattice_vectors_in_Bohr) # For debugging

# Number of atoms
atom_species_count = np.array(poscar_numpy_array[6])
total_number_of_atoms = atom_species_count.sum()
# print(total_number_of_atoms) # For debugging

# Coordinates of atoms
coordinates_of_atoms_poscar = poscar_numpy_array[8:]
fractional_atomic_coordinates_array = np.array(coordinates_of_atoms_poscar.tolist(), dtype=float)
# print(fractional_atomic_coordinates_array)

# Place the fractional_atomic_coordinates in columns
x_atom_coords, y_atom_coords, z_atom_coords = fractional_atomic_coordinates_array[:,0:3].T

# Multiply the fractional_atomic_coordinates in the columns with their respective
# lattice constants
x_atom_coords_in_Ang = x_atom_coords * scaled_lattice_vectors[0][0]
y_atom_coords_in_Ang = y_atom_coords * scaled_lattice_vectors[1][1]
z_atom_coords_in_Ang = z_atom_coords * scaled_lattice_vectors[2][2]

# convert the x_atom_coords_in_Ang to Bohr
x_atom_coords_in_Bohr = x_atom_coords_in_Ang / 0.529177
y_atom_coords_in_Bohr = y_atom_coords_in_Ang / 0.529177
z_atom_coords_in_Bohr = z_atom_coords_in_Ang / 0.529177

# for coord in range(11):
#     print(x_atom_coords_in_Bohr[coord], y_atom_coords_in_Bohr[coord], z_atom_coords_in_Bohr[coord])

# Zeros for the XV file
zeros = np.zeros((1,1))
zero = zeros[0]


#****************************
#   Writing the XV file     *
#****************************
two_space = " " * 2
four_space = " " * 4
eight_space = " " * 8
zero_values = eight_space+f"{zero[0]:.9f}" + eight_space+f"{zero[0]:.9f}" + eight_space+f"{zero[0]:.9f}"


def write_to_XV(output_file):
    with open(output_file, 'w') as xv_file:
#         # write lattice vectors
        for vector in lattice_vectors_in_Bohr:
            lattice_vector_Bohr = eight_space+f"{vector[0]:.9f}" + eight_space+f"{vector[1]:.9f}" + eight_space+f"{vector[2]:.9f}" + eight_space
            xv_file.write(lattice_vector_Bohr+zero_values+"\n")
        
        # Write total number of atoms
        xv_file.write(eight_space+f"{total_number_of_atoms}"+"\n")

        # Write atomic species index
        """ Change the line(s) below according to the file you are converting"""
        atomic_species_numbers = [1, 2, 3, 3, 3]
        atomic_species_nums = atomic_species_numbers * 20 # Multiply by 20 since we have 20 unit cells

        # Atomic numbers
        atomic_number = [82, 22, 8, 8, 8]
        atomic_numbers = atomic_number * 20

        # Write atomic coordinates in Bohr
        for coord in range(len(x_atom_coords_in_Bohr)):
            coords_atom_Bohr = f"{x_atom_coords_in_Bohr[coord]:.9f}"+four_space + \
                               f"{y_atom_coords_in_Bohr[coord]:.9f}"+four_space + \
                               f"{z_atom_coords_in_Bohr[coord]:.9f}"+four_space 
            
            atom_species = two_space+f"{atomic_species_nums[coord]}"+four_space

            atom_number = f"{atomic_numbers[coord]}" + four_space
            # xv_file.write(coords_atom_Bohr + zero_values+ "\n")
            xv_file.write(atom_species + atom_number + coords_atom_Bohr + zero_values+ "\n")


write_to_XV("PbTiO3.XV")


