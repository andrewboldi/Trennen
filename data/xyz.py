#!/usr/bin/python3.10
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from tqdm import tqdm
import os

inchis_file = open("iloveinchi.txt").readlines()

inchis = []
for line in inchis_file:
    inchis.append(line.split(", ")[0])

for i, inchi in tqdm(enumerate(inchis), total=len(inchis)):
    done = sorted(os.listdir("xyz/")) 
    if "{i:05d}.xyz" not in done:
        m = Chem.inchi.MolFromInchi(inchi)
        m = Chem.AddHs(m)

        AllChem.EmbedMolecule(m)

        _file = open(f"xyz/{i:05d}.xyz", "w")
        _file.write(Chem.MolToXYZBlock(m))
        _file.close()
