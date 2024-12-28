from pyxtal.symmetry import Symmetry

# Read the XYZ file into a PyXtal Structure object
structure = Structure.from_file("data/old_data/clean/1147.xyz")

# Create a Symmetry object and perform symmetry analysis
symmetry = Symmetry(structure)
point_group = symmetry.point_group

# Print the point group symbol
print(point_group)
