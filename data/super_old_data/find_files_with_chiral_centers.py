from rdkit import Chem
import os
import subprocess

for _file in os.listdir("files_with_stereochemistry/"):
    my_file = open("files_with_stereochemistry/" + _file, "r")
    lines = my_file.readlines()

    smiles = lines[len(lines) - 2].split("\t")[1]
    try:
        chiral_centers = Chem.FindMolChiralCenters(Chem.MolFromSmiles(smiles),includeUnassigned=True)
    except:
        pass
    if chiral_centers is not None:
        subprocess.call(["cp", f"{my_file.name}", "files_with_chiral_centers/"])
        print(f"Copied {my_file.name} to files_with_chiral_centers/")

    my_file.close()
